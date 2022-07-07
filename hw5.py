import cv2

image = cv2.imread('C:\\Users\\veanr\\Downloads\\pics\\videosframe15266.png')
cv2.imshow('Original',image)
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()

testimg = cv2.imwrite('C:\\Users\\veanr\\Downloads\\pics\\testimg.jpg', grayscale)
 
