import glob
import numpy as np
import cv2

# import all image files with the .png extension
images = sorted(glob.glob ("C:\\Users\\veanr\\Downloads\\src\\croppedframes\\*png"), key = len)
name = 0

while name+30 < len(images):
    imgs = images[name:name+30]

    image_data = []
    for img in images:
        this_image = cv2.imread(img, 1)
        image_data.append(this_image)
    avg_image = image_data[0]

    for i in range(len(image_data)):
        if i == 0:
            pass
        else:
       # for n in image_data:
    #    i = []
        # image_data.append(cv2.imread(n))
            alpha = 1.0/(i + 1)
            beta = 1.0 - alpha
            avg_image = cv2.addWeighted(np.array(image_data[i]), alpha, avg_image, beta, 0.0)
        
    cv2.imwrite(f'C:\\Users\\veanr\\Downloads\\src\\avgframes\\{name}.jpg', avg_image)
    name = name+ 1

    print(f'image {name} done')
