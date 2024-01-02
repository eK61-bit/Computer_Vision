# MUST BE RUN AS .py SCRIPT IN ORDER TO WORK.
# PLEASE MAKE SURE TO WATCH THE FULL VIDEO FOR THE EXPLANATION TO THIS NOTEBOOK
# TO BE CLEAR: RUNNING THIS CELL WILL KILL THE KERNEL IF YOU USE JUPYTER DIRECTLY

import cv2

img = cv2.imread('../DATA/00-puppy.jpg',cv2.IMREAD_GRAYSCALE)

while True:
    
# Show the image with OpenCV
    cv2.imshow('Puppy',img)
    
    if cv2.waitKey(1) & 0XFF == 27: 
        # Eğer 1 Milisaniye bekledik ve Kaşıç Tusuna Bastık
        # Klavye Tuslarına --> Varsayılan 27
        break        

# Wait for something on keyboard to be pressed to close window.
cv2.destroyAllWindows()