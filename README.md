# **Face Recognition System**

This Python script uses the `face_recognition` and `cv2` libraries to recognize faces from a video source (like a webcam) and match them to known faces.

## **How it works**

The script first encodes known faces from images stored in a directory named "faces". Each image file should contain a single face. The filename is used as the name of the person.

The script then captures video from a source (in this case, a webcam), detects faces in each frame, and tries to match them to the known faces. If a match is found, the script displays the name of the person and a confidence percentage on the video frame.

## **Usage**

1. Place images of the people you want to recognize in the "faces" directory. Each image should contain a single face. The filename (without the extension) will be used as the person's name.
2. Run the script with Python 3. It will start capturing video from your webcam and display the video frames in a window. Detected faces will be highlighted, and if a face matches a known face, the person's name and a confidence percentage will be displayed.
3. Press 'q' to quit the script.

## **Requirements**

- Python 3
- OpenCV (`cv2`)
- `face_recognition`
- `numpy`
- `math`
- `dlib==19.22`

## **Code Structure**

- `face_confidence`: This function calculates the confidence percentage of a face match.
- `FaceRecognition`: This class encapsulates the face recognition system.
    - `__init__`: The constructor encodes the known faces.
    - `encode_faces`: This method encodes the known faces from the images in the "faces" directory.
    - `run_recognition`: This method captures video, detects faces, matches them to the known faces, and displays the video frames with the face recognition results.
- The last two lines of the script create an instance of `FaceRecognition` and start the face recognition system.

## **Note**

This script uses the `face_recognition` library, which is built on top of `dlib`. The performance and accuracy of the face recognition can be affected by the quality of the input images and video, the lighting conditions, and the orientation of the faces.
