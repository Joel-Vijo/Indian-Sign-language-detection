# Indian-Sign-language-detection
Using computer vision to detect different signs in real time and output its meaning 




## Working
This project uses the built-in OpenCV function cv2.matchshapes() to detect the hand gestures. An input image is provided containing all the gestures for the digits 0-9. Using various techniques of image processing like masking and a Gaussian blur to smooth the image,the contours of the hand gestures are extracted. The same technique is used on the camera input to extract the contours of the hand in real time. This is then compared to the contours of the input image using cv2.matchshapes() which returns a value based on the Hu-moment values. A threshold value is set and the digit corresponding to the closest contour of the input image is displayed.  


## OpenCV functions used
Colour space conversion(BGR to HSV) \
Blurring(Smoothing) \
Morphological operation-dilation \
Contour detection \
cv2.matchShapes() 


## Input Image
![hands](https://user-images.githubusercontent.com/87753623/136809451-c7a45a4b-c93c-4ecb-8449-d2968bdd2b73.png)




## Demo
![sign_language](https://user-images.githubusercontent.com/87753623/136808775-ce24ed9f-6de1-47d3-8632-79053ebcee97.gif)
