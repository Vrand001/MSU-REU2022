import glob
import cv2
from cv2 import waitKey 
  
# path
path = r'C:\\Users\\veanr\\OneDrive\\Pictures\\0.png'
  
# Using cv2.imread() method
img = cv2.imread(path)
  
# Displaying the image
cv2.imshow('image', img)

waitKey(0)