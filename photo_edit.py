import cv2
import numpy as np 

def photoGet(name):
    image = cv2.imread("uploaded_images/"+name,0) 
    cv2.imwrite("uploaded_images/"+name,image) 
    
    cv2.imshow("new image",image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

