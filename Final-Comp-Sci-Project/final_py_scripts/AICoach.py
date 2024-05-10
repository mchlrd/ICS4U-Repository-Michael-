import cv2
import numpy as np
import time

import PoseModule as pm

cap = cv2.VideoCapture(0)
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
        per = np.interp(angle, (80, 345), (0, 100)) #TROUBLESHOOT THIS <------------
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
        cv2.rectangle(img, (0, 450), (250,720),(255,0,0), cv2.FILLED)
        cv2.putText(img, f'{int(count)}', (45,670), cv2.FONT_HERSHEY_PLAIN, 15, (255,255,255), 25)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'{int(fps)}', (50,100), cv2.FONT_HERSHEY_PLAIN, 5, (255,255,255), 5)
    cv2.imshow('Image', img)
    cv2.waitKey(1)