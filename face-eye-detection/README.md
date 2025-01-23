# Face and Eye Detection using OpenCV  

## Overview  
This project demonstrates real-time face and eye detection using a webcam. It leverages OpenCV's pre-trained Haar Cascade classifiers to identify facial and eye regions in a video feed. The application is interactive, where the user can exit the detection window by pressing the **'q'** key.  

## Features  
- **Real-Time Detection:** Detects faces and eyes in real-time using a webcam feed.  
- **Haar Cascades:** Utilizes pre-trained Haar Cascades for face and eye detection.  
- **Video Processing:** Efficient video frame processing using Python and OpenCV.  

## Technologies  
- **Programming Language:** Python  
- **Libraries:**  
  - OpenCV  
  - NumPy  

## Responsibilities  
- Integrated Haar Cascade classifiers for accurate face and eye detection.  
- Optimized the application for real-time video detection using efficient frame processing techniques.  

## Skills Demonstrated  
- Object detection using machine learning-based Haar Cascade models.  
- Video processing and real-time frame analysis.  

## Prerequisites  
Before running this project, ensure you have the following installed:  
- Python 3.x  
- OpenCV library  
- NumPy library  

## Installation and Setup  
1. Clone the repository:  
   ```bash  
   https://github.com/FahithKRM/OpenCV1/tree/main/face-eye-detection  
    ```
2. Navigate to the project folder:  
   ```bash  
   cd face-eye-detection    
    ```
3. Install the required libraries:  
   ```bash  
   pip install opencv-python numpy    
    ```

## Usage  
### Run the Python Script:  
  ```bash
  python face_eye_detection.py
  ``` 
1. Allow access to your webcam.  
2. The program will display a live video feed with:  
   - **Green rectangles** highlighting detected faces.  
   - **Blue rectangles** highlighting detected eyes.  
3. To exit, press the **'q'** key.  

## Code Explanation  
- **Face Detection:**  
  Utilizes the `haarcascade_frontalface_default.xml` classifier to detect faces in the video feed.  

- **Eye Detection:**  
  Detects eyes within the identified face regions using the `haarcascade_eye.xml` classifier.  

- **Video Feed Processing:**  
  Reads and processes each frame of the video feed from the webcam.  




