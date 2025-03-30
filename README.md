# Computer Vision
This repository contains solutions for various tasks related to computer vision, focusing on core algorithms and techniques commonly used in the field. These tasks were aimed at solving real-world problems such as object detection, feature matching, and camera calibration. *Note that some sections of the codes are based on templates provided.*
 
 Tasks include such topics:

  `#1:` HOG and Single Shot MultiBox Detector (SSD) detector  
        
        This task involves using HOG and SSD to detect objects (e.g., people and bottles) in both pre-recorded GIFs (or videos) and live webcam feeds. The goal is to identify objects in real-time or from a GIF/video, with bounding boxes drawn around the detected objects.

  `#2:` Robust line fitting using RANSAC, Matching Harris corner points and Matching (Speeded-Up Robust Features) SURF regions 
        Robust line fitting algorithm implemented using the RANSAC technique to handle outliers in data. Additionally, Harris corner points and SURF were used to detect and match key points in images, which are useful for tasks like image stitching and object recognition.
  
  `#3:` Homography using SIFT (Scale-Invariant Feature Transform) and KLT (Kanade-Lucas-Tomasi) tracker  
        Developed a homography estimation system using SIFT for feature matching and KLT tracker for real-time point tracking. This system can transform between different views of the same scene, commonly applied in tasks such as panorama stitching, motion tracking, and 3D reconstruction.
  
  `#4:` Camera calibration and Triangulation
        Developed a camera calibration algorithm using Direct Linear Transformation (DLT) to compute the intrinsic and extrinsic parameters of a camera, which is essential for tasks like 3D scene reconstruction and augmented reality applications. Additionally, worked on triangulation techniques to reconstruct 3D points from corresponding 2D points in multiple images, enabling the estimation of real-world coordinates from image data.

  `#5:` Fundamental matrix estimation and Two-view structure from motion
        Developed a fundamental matrix estimation method to model the relationship between two camera views and applied structure-from-motion techniques to reconstruct 3D models of scenes from multiple 2D image

