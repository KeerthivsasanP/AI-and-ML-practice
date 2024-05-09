import numpy as np
import cv2

blank_img = np.zeros((512,512,3))

#########################
### Write the function###
#########################

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(blank_img,(x,y),10,color=(0,200,0),thickness=-1)
    
##############################
## link the image and event ##
##############################
cv2.namedWindow(winname="blank_image")

cv2.setMouseCallback("blank_image",draw_circle)

####################
## Show the image ##
####################
while True:
    
    cv2.imshow("blank_image",blank_img)
    
    if cv2.waitKey(1) & 0xff == 27:
        break
        
cv2.destroyAllWindows()