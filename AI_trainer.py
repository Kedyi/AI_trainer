import cv2
import numpy as np
import time
import POSEMODULE as pm

cap = cv2.VideoCapture("videos/2.mp4")
detector = pm.poseDetector()
count=0
dir = 0  #direction up ...dir =1 (direction down)
pTime = 0

while True:

    success, img = cap.read()
    img = cv2.resize(img, (1000,500))
    img = detector.findPose(img,False)

    lmList = detector.findPosition(img, False)
    #print(lmList)

    if len(lmList) != 0:
        # 12 14 16-right
        # 11 13 15- left
        #Right Arm
        angle = detector.findAngle(img, 12, 14, 16)
        # # Left Arm
        # detector.findAngle(img, 11, 13, 15)
        per = np.interp(angle, (210,310),(0,100))
        #print(per)
        #print(angle)

        #check for curls
        if per==100:
            if dir ==0:
                count+=0.5
                dir=1
        if per ==0:
            if dir ==1:
                count+=0.5
                dir =0
        print(count)
        cv2.rectangle(img, (30,280),(200,450),(0,255,0),cv2.FILLED)
        cv2.putText(img, f'{int(count)}', (45,450), cv2.FONT_HERSHEY_PLAIN, 15,(255,0,0),25)

    cTime = time.time()
    fps=1/(cTime-pTime)
    pTime =cTime
    cv2.putText(img, str(int(fps)), (50,100), cv2.FONT_HERSHEY_PLAIN, 5,(255,0,0),5)


    cv2.imshow("Image", img)
    cv2.waitKey(1)