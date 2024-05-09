import cv2

img = cv2.imread("sample dataset/hummingBird.jpg")

while True:

    cv2.imshow("Hummingbird",img)
    
    #If we waited 1 ms and we pressed ESC key
    if cv2.waitKey(1) & 0xff==27:
        break
        
cv2.destroyAllWindows()
        
