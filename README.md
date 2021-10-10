# Indian-Sign-language-detection
Using computer vision to detect different sign language and output its meaning in real time




## Working
This project uses the built-in OpenCV function cv2.matchshapes() to detect the hand gestures. An input image is provided containing all the gestures for the digits 0-9. Using various techniques of image processing like masking and a Gaussian blur to smooth the image,the contours of the hand gestures are extracted. The same technique is used on the camera input to extract the contours of the hand in real time. This is then compared to the contours of the input image using cv2.matchshapes() which returns a value based on the Hu-moment values. A threshold value is set and the digit corresponding to the closest contour of the input image is displayed.  

