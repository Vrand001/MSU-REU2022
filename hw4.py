fruits=['apples','oranges','bananas','mangoes','grapes','strawberry']
print(fruits[-4:])


print('----------------------------------------------------------------------')

import glob
  
  
# Returns a list of names in list files.

import glob
import cv2
from cv2 import waitKey 
  
# path
path = r'C:\\Users\\veanr\\Downloads\\pics\\*png'
  
# Using cv2.imread() method
img = cv2.imread(path)
  
# Displaying the image
cv2.imshow('image', img)

waitKey(0)

print('----------------------------------------------------------------------')

lst=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
i = 0
while i < len(lst):
    if lst[i] == 100:
        print("There is a 100 at index no: " + str(i))
    i = i+1