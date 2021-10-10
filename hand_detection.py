import cv2
import numpy as np
cap = cv2.VideoCapture(0)
target=cv2.imread('hands.png')#input image containing all the gestures
grey1=cv2.cvtColor(target,cv2.COLOR_BGR2GRAY)
hsv2 = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)
lower = np.array([10,20,70],dtype=np.uint8)        
upper = np.array([20,255,255],dtype=np.uint8)

#getting a thresholded image containing only those pixels having skin color        
mask2 = cv2.inRange(hsv2, lower, upper)
       


mask2 = cv2.GaussianBlur(mask2,(3,3),50)#smoothing the image
c,hierarchy=cv2.findContours(mask2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#getting the contours
cnt2 = sorted(c, key=cv2.contourArea, reverse=True)#sorting the contours based on area

     
while(1):
        
          
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        grey2=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        #range of skin color
        lower_skin = np.array([0,30,0],dtype=np.uint8)
        upper_skin = np.array([148,255,255],dtype=np.uint8)
    
        mask = cv2.inRange(hsv, lower_skin, upper_skin)
       
        #to get a proper thresholded image of the hand
        kernel = np.ones((3,3),np.uint8)
        mask = cv2.dilate(mask,kernel,iterations = 3)
        mask = cv2.GaussianBlur(mask,(3,3),10)

        
    
        contours,hierarchy= cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#geting the contours
       
    
        
        cnt = sorted(contours, key=cv2.contourArea, reverse=True)#sorting the contours in descending order based on area

        #to detect 5
        area=cv2.contourArea(cnt[0])
        print(area)
        if (area>25000 and area<27000):
            cv2.putText(frame,str(5),(10,500), cv2.FONT_HERSHEY_SIMPLEX, 4, (0,0,255), 2, cv2.LINE_AA)
    
        
        frame=cv2.drawContours(frame,[cnt[0]],0,[0,255,0],3)#cnt[0] is the largest contour that is captured by the camera i.e the hand
        font = cv2.FONT_HERSHEY_SIMPLEX

        #looping over all the contours from the input image
        for i in range(0,10):
            ret = cv2.matchShapes(cnt[0],cnt2[i],1,0.0)#returns a value after comparing the respective contour of input image with that of our hand
            if(ret<0.09):#lower the value,more similar are the images
                #Based on the contour that matched,we print the value(except for 5)
                if(i==0):
                    cv2.putText(frame,str(9),(10,500), font, 4,(0,0,255),2,cv2.LINE_AA)
                    continue
                elif(i==1):
                    cv2.putText(frame,str(0),(10,500), font, 4,(0,0,255),2,cv2.LINE_AA)
                    continue
                elif(i==2):
                    cv2.putText(frame,str(6),(10,500), font, 4,(0,0,255),2,cv2.LINE_AA)
                    continue
                elif(i==3):
                    cv2.putText(frame,str(7),(10,500), font, 4,(0,0,255),2,cv2.LINE_AA)
                    continue
                elif(i==4 and area>23950):
                    cv2.putText(frame,str(4),(10,500), font, 4,(0,0,255),2,cv2.LINE_AA)
                    continue
                elif(i==5 and area<20000):
                    cv2.putText(frame,str(3),(10,500), font, 4,(0,0,255),2,cv2.LINE_AA)
                    continue
                elif(i==6):
                    cv2.putText(frame,str(8),(10,500), font, 4,(0,0,255),2,cv2.LINE_AA)
                    continue
                elif(i==7):
                    cv2.putText(frame,str(1),(10,500), font, 4,(0,0,255),2,cv2.LINE_AA)
                    continue
                elif(i==8):
                    cv2.putText(frame,str(2),(10,500), font, 4,(0,0,255),2,cv2.LINE_AA)
                    continue
                
                
           
            
        
            
        cv2.imshow('frame',frame)
        
    
        
    
        k = cv2.waitKey(5) & 0xFF#to exit from the window
        if k == 27:
            break
    
cv2.destroyAllWindows()
cap.release()    