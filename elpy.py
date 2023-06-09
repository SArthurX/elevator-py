import cv2
import mediapipe as mp
import angle
from floor import  hand_pos
import time
from pyfirmata2 import Arduino

#board = Arduino('COM5')
board = Arduino(Arduino.AUTODETECT)
pin =[5,6,7,8,9,10,11,12,13]

nled = {1,2,3,4,5,6,7,8,9}

drawingModule = mp.solutions.drawing_utils
drawingModule_styles = mp.solutions.drawing_styles
handLS = drawingModule.DrawingSpec(color=(65,220,0),thickness=5)
handCS = drawingModule.DrawingSpec(color=(175,77,131),thickness=7)

handsModule = mp.solutions.hands

cap = cv2.VideoCapture(0)            
fontFace = cv2.FONT_HERSHEY_SIMPLEX  
lineType = cv2.LINE_AA               

floor = set()
chfloor = set()

filfloor = [0]
num = int()

passtime = 0

try:
    print("Welcome to Contactless Pandemic Prevention Elevator System !")
    with handsModule.Hands(
        max_num_hands=1,
        model_complexity=0,
        min_detection_confidence=0.9,
        min_tracking_confidence=0.9) as hands:

        while (cap.isOpened()):
            ret, img = cap.read()

            x_l, x_r = 0, -300
            y_u, y_d = 0, -100
            img = img[y_u:y_d, x_l:x_r]
            w,h = img.shape[1],img.shape[0]

            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
            results = hands.process(imgRGB)                
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    drawingModule.draw_landmarks(img, hand_landmarks, handsModule.HAND_CONNECTIONS)

                    finger_points = []            
                    for i,lm in enumerate(hand_landmarks.landmark):
                        x = float(lm.x*w)
                        y = float(lm.y*h)

                        #print (i,x,y)

                        finger_points.append((x,y))

                    if finger_points:
                        finger_angle = angle.hand_angle(finger_points) 
                        #print(finger_angle)
                        if hand_pos(finger_angle) == 0:                   
                            cv2.putText(img, 'Confirm', (30,120), fontFace, 2, (255,255,255), 5, lineType)
                        elif hand_pos(finger_angle) == 44:                   
                            cv2.putText(img, 'Delete All', (30,120), fontFace, 2, (255,255,255), 5, lineType)
                        elif hand_pos(finger_angle) != None:
                            text = hand_pos(finger_angle)          
                            cv2.putText(img, str(text)+'F', (30,120), fontFace, 5, (255,255,255), 10, lineType)
                        board.digital[4].write(0)

                passtime += 1
                if(hand_pos(finger_angle) != 0):
                    if(passtime<30):
                        filfloor.append(hand_pos(finger_angle))   
                        num = max(filfloor,key=filfloor.count)
                    if passtime == 50:
                        floor.discard(hand_pos(finger_angle))
                        filfloor.clear()
                        cap.release()
                        time.sleep(2)
                        passtime = 0

                if(hand_pos(finger_angle) == 0):
                    floor.add(num)
                    filfloor.clear()
                    passtime = 0

                if (0 in floor or None in floor):
                    floor.discard(0)
                    floor.discard(None)
                    passtime = 0 
                    
                if (44 in floor):
                    floor.clear()
                    filfloor.clear()
                    passtime = 0 
                if(chfloor != floor):
                    chfloor = floor.copy()
                    print(chfloor)
            else:
                filfloor.clear()
                passtime = 0
                board.digital[4].write(1)
                
            for led in chfloor:
                board.digital[pin[led-1]].write(0)
            for l in nled.difference(chfloor):
                board.digital[pin[l-1]].write(1)

            cv2.imshow('sx', img)
            if(not cap.isOpened()):
                cap = cv2.VideoCapture(0) 
            if cv2.waitKey(5) == ord('q'):
                break
except KeyboardInterrupt:
    print("Elevator System END !")

cap.release()
cv2.destroyAllWindows()