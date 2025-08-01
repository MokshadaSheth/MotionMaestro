from django.shortcuts import render

import subprocess
import webbrowser
import mediapipe as mp
import cv2
import numpy as np
import pyautogui
import time
import cvzone
import pydirectinput
from cvzone.HandTrackingModule import HandDetector

def index(request):
    return render(request,'index.html')

def hcr(request):
    pyautogui.press('win')
    # Type the text you want to input
    text_to_type = "Hill Climb Racing"
    pyautogui.typewrite(text_to_type)

    # Wait for a few seconds to give you time to focus on the target window
    time.sleep(2)
    # Press the Enter key
    pyautogui.press('enter')

    def execHandTab():
        # Variables
        width, height = 500, 500

        # Camera setup
        cap = cv2.VideoCapture(0)
        cap.set(3, width)
        cap.set(4, height)

        # Hand Detector
        detector = HandDetector(detectionCon=0.8, maxHands=2)

        while True:
            try:
                # Import images
                success, img = cap.read()
                img = cv2.flip(img, 1)

                hands, img = detector.findHands(img)

                if hands and len(hands) == 1:
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    print(fingers)
                    lmList = hand['lmList']

                    # Constrain value for easier drawing
                    indexFinger = lmList[8][0], lmList[8][1]
                    xVal = int(np.interp(lmList[8][0], [width // 2, width], [0, width]))
                    yVal = int(np.interp(lmList[8][1], [150, height - 150], [0, height]))

                    indexFinger = xVal, yVal

                    # Gesture1
                    if fingers == [1, 1, 1, 1, 1]:
                        pydirectinput.keyUp('left')  # Press the "Down" key when grid 1, 1 is encountered
                        pydirectinput.keyDown('right')  # Press the "Down" key when grid 1, 1 is encountered


                    # Gesture1
                    # Thumb = Open FaceBook
                    elif fingers == [0, 0, 0, 0, 0]:
                        pydirectinput.keyUp('right')  # Press the "Down" key when grid 1, 1 is encountered
                        pydirectinput.keyDown('left')  # Press the "Down" key when grid 1, 1 is encountered

                    else:
                        pydirectinput.keyUp('right')  # Press the "Down" key when grid 1, 1 is encountered
                        pydirectinput.keyUp('left')  # Press the "Down" key when grid 1, 1 is encountered


            except BrokenPipeError as e:
                pass

            cv2.imshow("Image", img)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
        cv2.destroyAllWindows()

    execHandTab()
    return render(request,'index.html')



def tet(request):
    pyautogui.press('win')
    # Type the text you want to input
    text_to_type = "Tetris"
    pyautogui.typewrite(text_to_type)

    # Wait for a few seconds to give you time to focus on the target window
    time.sleep(2)
    # Press the Enter key
    pyautogui.press('enter')

    def execHandTab():

        # Variables
        width, height = 500, 500

        # Camera setup
        cap = cv2.VideoCapture(0)
        cap.set(3, width)
        cap.set(4, height)

        # Variables
        imgNumber = 0
        hs, ws = int(120 * 1), 213
        gestureThreshold = 300
        buttonPressed = False
        buttonCounter = 0
        buttonDelay = 30
        annotations = [[]]
        annotationNumber = -1
        annotationStart = False

        # Hand Detector
        detector = HandDetector(detectionCon=0.8, maxHands=2)

        while True:
            try:
                # Import images
                success, img = cap.read()
                img = cv2.flip(img, 1)

                hands, img = detector.findHands(img)

                if hands and len(hands) == 1:
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    print(fingers)
                    lmList = hand['lmList']

                    # Constrain value for easier drawing
                    indexFinger = lmList[8][0], lmList[8][1]
                    xVal = int(np.interp(lmList[8][0], [width // 2, width], [0, width]))
                    yVal = int(np.interp(lmList[8][1], [150, height - 150], [0, height]))

                    indexFinger = xVal, yVal

                    # Gesture1
                    if fingers == [1, 1, 0, 0, 0]:
                        pydirectinput.keyDown('left')  # Press the "Down" key when grid 1, 1 is encountered
                        time.sleep(0.4)
                        pydirectinput.keyUp('left')  # Press the "Down" key when grid 1, 1 is encountered

                    # Gesture1
                    # Thumb = Open FaceBook
                    elif fingers == [0, 1, 0, 0, 1]:
                        pydirectinput.keyUp('left')  # Press the "Down" key when grid 1, 1 is encountered
                        pydirectinput.keyDown('right')  # Press the "Down" key when grid 1, 1 is encountered
                        time.sleep(0.4)
                        pydirectinput.keyUp('right')  # Press the "Down" key when grid 1, 1 is encountered

                    elif fingers == [0, 1, 1, 1, 0]:
                        pydirectinput.keyUp('left')  # Press the "Down" key when grid 1, 1 is encountered
                        pydirectinput.keyUp('right')  # Press the "Down" key when grid 1, 1 is encountered
                        pydirectinput.keyDown('up')  # Press the "Down" key when grid 1, 1 is encountered
                        time.sleep(0.4)
                        pydirectinput.keyUp('up')  # Press the "Down" key when grid 1, 1 is encountered


                    elif fingers == [1, 1, 1, 1, 0]:
                        pydirectinput.keyUp('left')  # Press the "Down" key when grid 1, 1 is encountered
                        pydirectinput.keyUp('right')  # Press the "Down" key when grid 1, 1 is encountered
                        pydirectinput.keyDown('down')  # Press the "Down" key when grid 1, 1 is encountered
                        time.sleep(0.4)
                        pydirectinput.keyUp('down')  # Press the "Down" key when grid 1, 1 is encountered

            except BrokenPipeError as e:
                pass

            cv2.imshow("Image", img)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
        cv2.destroyAllWindows()

    execHandTab()
    return render(request,'index.html')


def carsi(request):
    pyautogui.press('win')
    # Type the text you want to input
    text_to_type = "City Racing"
    pyautogui.typewrite(text_to_type)

    # Wait for a few seconds to give you time to focus on the target window
    time.sleep(2)
    # Press the Enter key
    pyautogui.press('enter')

    cap = cv2.VideoCapture(0)

    mpHands = mp.solutions.hands
    hands_mp = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils

    detector = HandDetector(detectionCon=0.8, maxHands=2)

    pTime = 0
    cTime = 0

    while True:
        try:
            success, img = cap.read()
            img = cv2.flip(img, 1)
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Detect hands using the cvzone HandDetector
            hands_cvzone, img = detector.findHands(img)

            if hands_cvzone and len(hands_cvzone) == 1:
                pass

            if hands_cvzone and len(hands_cvzone) > 1:
                hand1 = hands_cvzone[0]
                fingers1 = detector.fingersUp(hand1)
                hand2 = hands_cvzone[1]
                fingers2 = detector.fingersUp(hand2)

                # Process hands using the mediapipe Hands object
                results = hands_mp.process(imgRGB)

                flag1 = 0
                if results.multi_hand_landmarks:
                    for handLms in results.multi_hand_landmarks:
                        for id, lm in enumerate(handLms.landmark):
                            h, w, c = img.shape
                            cx, cy = int(lm.x * w), int(lm.y * h)
                            print(id, cx, cy)

                            if id == 4:
                                cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)

                        mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

                        # Divide the screen into three parts (left, middle, right)
                        if fingers1 == [1, 0, 0, 0, 0] and fingers2 == [1, 0, 0, 0, 0]:
                                flag1 = 1
                                cv2.putText(img, 'Accelerate Left', (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                                pydirectinput.keyUp('down')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyUp('left')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyUp('right')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyDown('up')  # Press the "Down" key when grid 1, 1 is encountered
                                time.sleep(0.5)
                                pydirectinput.keyUp('up')  # Press the "Down" key when grid 1, 1 is encountered


                        elif fingers1 == [1, 1, 1, 0, 0] and fingers2 == [1, 1, 1, 0, 0]:
                                flag1 = -1
                                cv2.putText(img, 'Brake', (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                                pydirectinput.keyUp('up')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyDown('left')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyDown('down')  # Press the "Down" key when grid 1, 1 is encountered
                                time.sleep(0.5)
                                pydirectinput.keyUp('left')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyUp('down')  # Press the "Down" key when grid 1, 1 is encountered


                        elif fingers1 == [1, 0, 0, 0, 1] and fingers2 == [1, 0, 0, 0, 1]:
                                pydirectinput.keyDown('up')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyDown('left')  # Press the "Down" key when grid 1, 1 is encountered
                                time.sleep(0.3)
                                pydirectinput.keyUp('down')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyUp('up')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyUp('left')  # Press the "Down" key when grid 1, 1 is encountered

                        elif fingers1 == [1, 1, 0, 0, 0] and fingers2 == [1, 1, 0, 0, 0]:
                                pydirectinput.keyDown('up')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyDown('right')  # Press the "Down" key when grid 1, 1 is encountered
                                time.sleep(0.3)
                                pydirectinput.keyUp('up')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyUp('down')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyUp('right')  # Press the "Down" key when grid 1, 1 is encountered

                        elif fingers1 == [1, 1, 1, 0, 0] and fingers2 == [1, 1, 1, 0, 0]:
                                cv2.putText(img, 'Brake', (w // 2 - 15, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                                pydirectinput.keyUp('up')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyUp('left')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyUp('right')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyDown('down')  # Press the "Down" key when grid 1, 1 is encountered
                                time.sleep(0.5)
                                pydirectinput.keyUp('down')  # Press the "Down" key when grid 1, 1 is encountered

                    # Draw grid lines
                    cv2.line(img, (int(w * 0.2), 0), (int(w * 0.2), h), (0, 255, 0), 2)
                    cv2.line(img, (int(w * 0.8), 0), (int(w * 0.8), h), (0, 255, 0), 2)

        except BrokenPipeError as e:
            pass

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # Display FPS
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return render(request,'index.html')

def mbi(request):
    pyautogui.press('win')
    # Type the text you want to input
    text_to_type = "Motoracing"
    pyautogui.typewrite(text_to_type)

    # Wait for a few seconds to give you time to focus on the target window
    time.sleep(2)
    # Press the Enter key
    pyautogui.press('enter')

    cap = cv2.VideoCapture(0)

    mpHands = mp.solutions.hands
    hands_mp = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils

    detector = HandDetector(detectionCon=0.8, maxHands=2)

    pTime = 0
    cTime = 0

    while True:
        try:
            success, img = cap.read()
            img = cv2.flip(img, 1)
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Detect hands using the cvzone HandDetector
            hands_cvzone, img = detector.findHands(img)

            if hands_cvzone and len(hands_cvzone) == 1:
                pass

            if hands_cvzone and len(hands_cvzone) > 1:
                hand1 = hands_cvzone[0]
                fingers1 = detector.fingersUp(hand1)
                hand2 = hands_cvzone[1]
                fingers2 = detector.fingersUp(hand2)

                # Process hands using the mediapipe Hands object
                results = hands_mp.process(imgRGB)

                if results.multi_hand_landmarks:
                    for handLms in results.multi_hand_landmarks:
                        for id, lm in enumerate(handLms.landmark):
                            h, w, c = img.shape
                            cx, cy = int(lm.x * w), int(lm.y * h)
                            print(id, cx, cy)

                            if id == 4:
                                cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)

                        mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

                        # Divide the screen into three parts (left, middle, right)
                        if cx < w * 0.2:  # Part 1 (20%)
                            if fingers1 == [1, 0, 0, 0, 0] and fingers2 == [1, 0, 0, 0, 0]:
                                cv2.putText(img, 'Accelerate Left', (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                                pydirectinput.keyDown('left')  # Press the "Down" key when grid 1, 1 is encountered
                                time.sleep(0.5)
                                pydirectinput.keyUp('left')  # Press the "Down" key when grid 1, 1 is encountered


                            elif fingers1 == [1, 1, 1, 0, 0] and fingers2 == [1, 1, 1, 0, 0]:
                                cv2.putText(img, 'Brake', (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                                pydirectinput.keyUp('up')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyDown('left')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyDown('down')  # Press the "Down" key when grid 1, 1 is encountered
                                time.sleep(0.5)
                                pydirectinput.keyUp('left')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyUp('down')  # Press the "Down" key when grid 1, 1 is encountered

                        flag1 = 0
                        if cx > w * 0.8:  # Part 3 (20%)

                            if fingers1 == [1, 0, 0, 0, 0] and fingers2 == [1, 0, 0, 0, 0]:
                                pydirectinput.keyUp('left')  # Press the "Down" key when grid 1, 1 is encountered
                                cv2.putText(img, 'Accelerate Right', (w - 40, 30), cv2.FONT_HERSHEY_PLAIN, 2,
                                            (255, 0, 0), 2)
                                pydirectinput.keyDown('right')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyDown('up')
                                time.sleep(0.5)
                                pydirectinput.keyUp('up')
                                pydirectinput.keyUp('right')  # Press the "Down" key when grid 1, 1 is encountered


                            elif fingers1 == [1, 1, 1, 0, 0] and fingers2 == [1, 1, 1, 0, 0]:
                                cv2.putText(img, 'Brake Right', (w - 40, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                                pydirectinput.keyUp('up')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyDown('right')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyDown('down')  # Press the "Down" key when grid 1, 1 is encountered
                                time.sleep(0.5)
                                pydirectinput.keyUp('right')  # Press the "Down" key when grid 1, 1 is encountered

                        if cx >= w * 0.2 and cx <= w * 0.8:  # Part 2 (60%)
                            if fingers1 == [1, 0, 0, 0, 1] and fingers2 == [1, 0, 0, 0, 1]:
                                pydirectinput.keyDown('left')  # Press the "Down" key when grid 1, 1 is encountered
                                flag1 = 1
                                time.sleep(0.3)
                                pydirectinput.keyUp('down')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyDown('up')  # Press the "Down" key when grid 1, 1 is encountered

                            if fingers1 == [1, 1, 0, 0, 0] and fingers2 == [1, 1, 0, 0, 0]:
                                pydirectinput.keyDown('right')  # Press the "Down" key when grid 1, 1 is encountered
                                flag1 = 2
                                time.sleep(0.3)
                                pydirectinput.keyUp('down')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyDown('up')  # Press the "Down" key when grid 1, 1 is encountered

                            if fingers1 == [1, 0, 0, 0, 0] and fingers2 == [1, 0, 0, 0, 0]:
                                cv2.putText(img, 'Accelerate', (w // 2 - 15, 30), cv2.FONT_HERSHEY_PLAIN, 2,
                                            (255, 0, 0), 2)
                                pydirectinput.keyUp('down')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyUp('left')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyUp('right')
                                pydirectinput.keyDown('up')  # Press the "Down" key when grid 1, 1 is encountered


                            elif fingers1 == [1, 1, 1, 0, 0] and fingers2 == [1, 1, 1, 0, 0]:
                                cv2.putText(img, 'Brake', (w // 2 - 15, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                                pydirectinput.keyUp('up')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyUp('left')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyUp('right')  # Press the "Down" key when grid 1, 1 is encountered
                                pydirectinput.keyDown('down')  # Press the "Down" key when grid 1, 1 is encountered

                    # Draw grid lines
                    cv2.line(img, (int(w * 0.2), 0), (int(w * 0.2), h), (0, 255, 0), 2)
                    cv2.line(img, (int(w * 0.8), 0), (int(w * 0.8), h), (0, 255, 0), 2)

        except BrokenPipeError as e:
            pass

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # Display FPS
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return render(request,'index.html')


class FaceMeshDetector():
    def __init__(self,static_image_mode=False,max_num_faces=1,refine_landmarks=False,min_detection_confidence=0.5,min_tracking_confidence=0.5):

                self.static_image_mode=False,
                self.max_num_faces=1,
                self.refine_landmarks=False,
                self.min_detection_confidence=0.5,
                self.min_tracking_confidence=0.5

                self.mpDraw = mp.solutions.drawing_utils
                self.mpFaceMesh = mp.solutions.face_mesh
                self.faceMesh = self.mpFaceMesh.FaceMesh(max_num_faces=2)
                self.drawSpec = self.mpDraw.DrawingSpec(thickness=1,circle_radius=1)


    def findFaceMesh(self,img,draw=True):
        imgRGB = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
        results = self.faceMesh.process(imgRGB)
        if results.multi_face_landmarks:
            for faceLms in results.multi_face_landmarks:
                self.mpDraw.draw_landmarks(img, faceLms , self.mpFaceMesh.FACEMESH_CONTOURS , self.drawSpec,self.drawSpec)

                for id , lm in enumerate(faceLms.landmark):
                    print(lm)
                    ih , iw , ic = img.shape
                    x,y = int(lm.x*iw) , int(lm.y*ih)
                    print(id ,x,y)
        return img

def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = FaceMeshDetector()
    while True:
        success, img = cap.read()
        img = detector.findFaceMesh(img)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS : {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break


    cv2.destroyAllWindows()

if __name__=="__main__":
    main()

def ssurf(request):
    class handDetector():
        def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
            self.mode = mode
            self.maxHands = maxHands
            self.detectionCon = detectionCon
            self.trackCon = trackCon

            self.mpHands = mp.solutions.hands
            self.hands = self.mpHands.Hands(self.mode, self.maxHands)
            self.mpDraw = mp.solutions.drawing_utils

        def findHands(self, img, draw=True):
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.results = self.hands.process(imgRGB)

            if self.results.multi_hand_landmarks:
                for handLms in self.results.multi_hand_landmarks:
                    if draw:
                        # mediapipe method that helps to draw points of hands
                        self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

            return img

        def findPosition(self, img, handNo=0, draw=True):
            lmList = []
            if self.results.multi_hand_landmarks:
                myHand = self.results.multi_hand_landmarks[handNo]
                for id, lm in enumerate(myHand.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    print(id, cx, cy)
                    lmList.append([id, cx, cy])
                    if draw:
                        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
            return lmList

    def main():
        pTime = 0
        cTime = 0
        cap = cv2.VideoCapture(0)
        detector = handDetector()

        while True:
            success, img = cap.read()
            img = detector.findHands(img)
            lmList = detector.findPosition(img)

            if len(lmList) != 0:
                print(lmList[4])

            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime

            # Display FPS
            cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

            cv2.imshow("Image", img)
            key = cv2.waitKey(1)
            if key is ord('q'):
                break

    class FaceMeshDetector():
        def __init__(self, static_image_mode=False, max_num_faces=1, refine_landmarks=False,
                     min_detection_confidence=0.3, min_tracking_confidence=0.3):
            self.static_image_mode = static_image_mode
            self.max_num_faces = max_num_faces
            self.refine_landmarks = refine_landmarks
            self.min_detection_confidence = min_detection_confidence
            self.min_tracking_confidence = min_tracking_confidence

            self.mpDraw = mp.solutions.drawing_utils
            self.mpFaceMesh = mp.solutions.face_mesh
            self.faceMesh = self.mpFaceMesh.FaceMesh(
                static_image_mode=self.static_image_mode,
                max_num_faces=self.max_num_faces,
                refine_landmarks=self.refine_landmarks,
                min_detection_confidence=self.min_detection_confidence,
                min_tracking_confidence=self.min_tracking_confidence
            )
            self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)

            # Define ROIs for each grid cell
            self.grid_roi = {
                'Grid1': (0, 0, 1 / 3, 1 / 3),
                'Grid2': (1 / 3, 0, 2 / 3, 1 / 3),
                'Grid3': (2 / 3, 0, 1, 1 / 3),
                'Grid4': (0, 1 / 3, 1 / 3, 2 / 3),
                'Grid5': (1 / 3, 1 / 3, 2 / 3, 2 / 3),
                'Grid6': (2 / 3, 1 / 3, 1, 2 / 3),
                'Grid7': (0, 2 / 3, 1 / 3, 1),
                'Grid8': (1 / 3, 2 / 3, 2 / 3, 1),
                'Grid9': (2 / 3, 2 / 3, 1, 1),
            }

        def open_processes(self):
            # Open abc.exe and def.exe using subprocess.Popen()
            abc_process = subprocess.Popen("Subway Surfers.exe")
            def_process = subprocess.Popen("Keyboard_controls.exe")
            return abc_process, def_process

        def kill_processes(self, *processes):
            # Kill both processes using psutil
            for process in processes:
                process.terminate()
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    process.kill()

        def findFaceMesh(self, img, draw=True):
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = self.faceMesh.process(imgRGB)

            grid_values = {}

            if results.multi_face_landmarks:
                for faceLms in results.multi_face_landmarks:

                    if draw:
                        self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_CONTOURS, self.drawSpec,
                                                   self.drawSpec)

                    for id, lm in enumerate(faceLms.landmark):
                        ih, iw, ic = img.shape
                        x, y = int(lm.x * iw), int(lm.y * ih)

                        # Calculate the grid coordinates based on X and Y coordinates
                        grid_x = int(lm.x * 3)
                        grid_y = int(lm.y * 3)

                        # Assign a specific value to the grid cell where the face mesh is located
                        grid_values[(grid_x, grid_y)] = self.get_grid_value(grid_x, grid_y)

            # Draw the grid ROIs on the image
            for name, roi in self.grid_roi.items():
                x1, y1, x2, y2 = int(roi[0] * img.shape[1]), int(roi[1] * img.shape[0]), int(
                    roi[2] * img.shape[1]), int(
                    roi[3] * img.shape[0])
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

            return img, grid_values

        def get_grid_value(self, x, y):
            if x == 0 and y == 0:
                return 11
            elif x == 1 and y == 0:
                return 21
            elif x == 0 and y == 1:
                return 12
            elif x == 1 and y == 1:
                return 22
            elif x == 2 and y == 1:
                return 32
            elif x == 0 and y == 2:
                return 21
            elif x == 2 and y == 0:
                return 31
                return 13
            elif x == 1 and y == 2:
                return 23
            elif x == 2 and y == 2:
                return 33
            else:
                return 0

    def main():
        cap = cv2.VideoCapture(0)
        pTime = 0
        detector2 = handDetector()
        # Open the processes
        detector = FaceMeshDetector()
        abc_process, def_process = detector.open_processes()

        while True:
            success, img = cap.read()
            img = cv2.flip(img, 1)
            img, grid_values = detector.findFaceMesh(img, draw=False)
            img = detector2.findHands(img)
            lmList = detector2.findPosition(img, draw=False)  # Disable drawing landmarks for better performance

            if len(lmList) != 0:
                print(lmList[4])

            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(img, f'FPS : {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

            # Print the grid values
            for (x, y), value in grid_values.items():
                print(f'Grid{x + 1}-{y + 1}: {value}')

                # Check for the specific grid cell (1, 0) with value 21
                if x == 1 and y == 0 and value == 21:
                    time.sleep(0.1)
                    # Press the "Up" key
                    pydirectinput.press('up')  # Press the "Down" key when grid 1, 1 is encountered

                # Check for the specific grid cell (1, 1) with value 22
                elif x == 1 and y == 2 and value == 23:
                    # Press the "Down" key
                    pydirectinput.press('down')  # Press the "Down" key when grid 1, 1 is encountered
                    time.sleep(0.1)

                # Check for the specific grid cell (1, 1) with value 22
                elif x == 0 and y == 1 and value == 12:
                    # Press the "Left" key
                    pydirectinput.press('left')  # Press the "Down" key when grid 1, 1 is encountered
                    time.sleep(0.1)

                # Check for the specific grid cell (1, 1) with value 22
                elif x == 2 and y == 1 and value == 32:
                    # Press the "Right" key
                    pydirectinput.press('right')  # Press the "Down" key when grid 1, 1 is encountered
                    time.sleep(0.1)

            cv2.imshow("Image", img)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break

        # Kill the processes
        detector.kill_processes(abc_process, def_process)
        cv2.destroyAllWindows()

    main()
    return render(request, 'index.html')
