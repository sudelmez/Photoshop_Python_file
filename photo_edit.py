import cv2
import numpy as np 

def getShop(image):
    img = image
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )
    return img


