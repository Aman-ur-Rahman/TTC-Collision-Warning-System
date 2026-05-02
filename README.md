#  Vision-Based Time-To-Collision (TTC) Collision Warning System

#Overview

This project implements a **vision-based collision warning system** using **YOLOv8 object detection** and **Time-To-Collision (TTC)** estimation.
It analyzes video input, detects vehicles, estimates their relative motion, and generates real-time alerts indicating collision risk.

---

#Objective

To develop a simple system that can:

* Detect vehicles in a video stream
* Estimate relative motion using bounding box changes
* Calculate **Time-To-Collision (TTC)**
* Provide visual warnings (SAFE / WARNING / BRAKE)

---

# How It Works

1. **Object Detection**
   Uses YOLOv8 to detect vehicles in each frame.

2. **Distance Approximation**
   Bounding box area is used as an approximate indicator of distance.

3. **Relative Speed Estimation**
   Change in bounding box area over time is used to estimate speed.

4. **TTC Calculation**
   TTC is computed as:

   ```
   TTC = Area / Rate of Change of Area
   ```

5. **Collision Warning**

   *  **BRAKE** → TTC < 2 seconds
   *  **WARNING** → TTC < 4 seconds
   *  **SAFE** → TTC ≥ 4 seconds

---

#Technologies Used

* Python
* OpenCV
* Ultralytics YOLOv8
* NumPy

---

# Project Structure

```
project/
│── main.py
│── videoplayback1.mp4
│── README.md
```

---

# How to Run

1. Install dependencies:

   ```bash
   pip install ultralytics opencv-python
   ```

2. Run the program:

   ```bash
   python main.py
   ```

3. Press **'f'** to exit the video window.

---

# Output

* Bounding boxes around detected vehicles
* Real-time TTC displayed
* Collision risk status shown on screen

*(Add screenshots here for better presentation)*

---

# Limitations

* Uses bounding box area as an approximation (not real-world distance)
* No advanced object tracking (simple estimation)
* Accuracy depends on video quality and detection performance

---

# Conclusion

This project demonstrates a **basic ADAS-inspired module** for collision warning using computer vision techniques.
It highlights how TTC can be estimated using visual cues in real-time.

---

# Author
Aman ur Rahman
