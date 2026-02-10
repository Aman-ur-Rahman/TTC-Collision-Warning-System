import cv2 as cv
import time
from ultralytics import YOLO

def decide_ttc(ttc):
  if ttc<2.0:
    return "BRAKE",(0,0,255)
  
  elif ttc<4.0:
    return "WARNING",(0,165,255)
  
  else:
    return "SAFE",(0,255,0)
  
  
cap=cv.VideoCapture('videoplayback1.mp4')
model = YOLO("yolov8n.pt")
obstucles={0,1,2,3,5,7}

prev_area=0
prev_time=time.time()


while True:
  ret,frame=cap.read()
  if not ret:
    break

  results=model(frame,verbose=False)
  for box in results[0].boxes:
    x1,y1,x2,y2=map(int,box.xyxy[0])
    cls=int(box.cls[0])
    conf=float(box.conf[0])
    if conf<0.5:
      continue
    if  cls not in obstucles:
      continue

    area=(x2-x1)*(y2-y1)
    area_change=area-prev_area
    current_time=time.time()
    dt =current_time-prev_time

    if dt>0:
      speed=area_change/dt
    else:
      speed=0

    if speed>0:
      ttc=area/speed
    else:
      ttc=float('inf')
    
    status,color=decide_ttc(ttc)
    cv.rectangle(frame,(x1,y1),(x2,y2),color,2)
    
      


    cv.putText(frame, f"Time for impact: {ttc:.2f}s", (x1, y1-30),
                cv.FONT_HERSHEY_SIMPLEX,
                0.8, (color), 2)
    
    cv.putText(frame,f"Collision Risk:{status}",(30,80),
               cv.FONT_HERSHEY_SIMPLEX,1.0,color,3)
    
    cv.putText(frame, f"Area: {area}", (x1, y1),
                cv.FONT_HERSHEY_SIMPLEX,
                0.7, (color), 2)
    prev_area = area
    prev_time = current_time
    
   
 
  cv.imshow('videoplayback1.mp4',frame)
  
  if cv.waitKey(30) & 0xff==ord('f'):
    break
cap.release()
cv.destroyAllWindows()