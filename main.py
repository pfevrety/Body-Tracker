import time

import cv2
import mediapipe as mp

import HandTracking as ht

pTime = 0
cTime = 0

cap = cv2.VideoCapture(0)

detector = ht.handDetector()

# Check if camera opened successfully
if cap.isOpened() == False:
    print("Error opening video stream or file")

while cap.isOpened():
    ret, img = cap.read()

    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        print(lmList[4])
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    img = cv2.flip(img, 1)
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 3, (255, 0, 255), 3)

    cv2.imshow('Frame', img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
