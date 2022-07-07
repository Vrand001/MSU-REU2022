import cv2
import numpy as np
import os
from os import listdir
import glob

# imdir = 'C:\\Users\\veanr\\Downloads\\src\\frames'
# ext = [ 'jpg']    # Add image formats here

# files = []
# [files.extend(glob.glob(imdir + '*.' + e)) for e in ext]

# images = [cv2.imread(file) for file in files]

# Read image
# import the modules


# get the path or directory
# folder_dir = "C:\\Users\\veanr\\Downloads\\src\\frames"
# for images in os.listdir(folder_dir):

# 	# check if the image end swith png or jpg or jpeg
# 	if (images.endswith(".png") or images.endswith(".jpg")\
# 		or images.endswith(".jpeg")):
# 		# display
# 		print(images)

image = cv2.imread("C:\\Users\\veanr\\Downloads\\src\\frames\\frames10.jpg")

# Select ROI
r = cv2.selectROI("select the area", image)

frameNr = 0

for image_path in sorted(glob.glob("C:\\Users\\veanr\\Downloads\\src\\frames\\*.jpg"), key = len):
    images = cv2.imread(image_path)
    # print(image_path)
    cropped_image = images[int(r[1]):int(r[1]+r[3]),
					int(r[0]):int(r[0]+r[2])]
    cv2.imwrite(f'.\\croppedframes\\{frameNr}.png', cropped_image)
    frameNr = frameNr + 1
    print("its working")

# # Display cropped image
# cv2.imshow("Cropped image", cropped_image)
