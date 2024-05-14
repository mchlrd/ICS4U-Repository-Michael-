import cv2
import numpy as np
import time

import PoseModule as pm

cap = cv2.VideoCapture(r'C:\Users\Michael\Documents\compsci_grade12\ICS4U-Repository-Michael-\Final-Comp-Sci-Project\aicoachmp4s\6.mp4')
detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280,720))
    #img = cv2.imread('aicoachmp4s/2.jpg')
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    #print(lmList)

    if len(lmList) != 0:
        #Left arm
        angle = detector.findAngle(img, 11, 13, 15)
        per = np.interp(angle, (200, 315), (0, 100)) #TROUBLESHOOT THIS <------------
        #print(angle, per)
        
        #check for reps

        if per == 100:
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            if dir == 1:
                count += 0.5
                dir = 0

        print(count)
        cv2.putText(img, f'{int(count)}', (45,670), cv2.FONT_HERSHEY_PLAIN, 12, (255,255,255), 25)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.imshow('Image', img)
    cv2.waitKey(1)