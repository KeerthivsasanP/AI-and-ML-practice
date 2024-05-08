import cv2
import numpy as np

##############
## variable ##
###############
ix,iy = -1,-1
isDrawing = False

##############
## Function ##
##############

def draw_rectangle(event,x,y,flags,param):
    global ix,iy,isDrawing
    
    if event == cv2.EVENT_LBUTTONDOWN:
        isDrawing = True
        ix,iy = x,y
        
    elif event == cv2.EVENT_MOUSEMOVE and isDrawing == True:
        cv2.rectangle(blank_img,(ix,iy),(x,y),color=(0,0,255),thickness=-1)
        
    elif event == cv2.EVENT_LBUTTONUP:
        isDrawing = False
        cv2.rectangle(blank_img,(ix,iy),(x,y),color=(0,0,255),thickness=-1)
        
        

################
## Show image ##
################

blank_img = np.zeros((512,512,3))
cv2.namedWindow("drag_image")
cv2.setMouseCallback("drag_image",draw_rectangle)

while True:
    cv2.imshow("drag_image",blank_img)
    
    if cv2.waitKey(1) & 0xff == 27:
        break
        
cv2.destroyAllWindows()