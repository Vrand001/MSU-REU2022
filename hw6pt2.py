import cv2
 
capture = cv2.VideoCapture('C:\\Users\\veanr\\Downloads\\src\\Ellicott City 2018 Flood Multicam  REVISED-CgVRnrk4Rv8.mp4.part')
 
frameNr = 0
 
while (True):
 
    success, frame = capture.read()
 
    if success:
        cv2.imwrite(f'C:\\Users\\veanr\\Downloads\\src\\frames{frameNr}.jpg', frame)
 
    else:
        break
 
    frameNr = frameNr+1
 
capture.release()