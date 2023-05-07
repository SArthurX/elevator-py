import cv2
import mediapipe as mp
import angle
from floor import  hand_pos
import time

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)            
fontFace = cv2.FONT_HERSHEY_SIMPLEX  
lineType = cv2.LINE_AA               

floor = set()
chfloor = set()
passtime = 0

with mp_hands.Hands(
    max_num_hands=1,
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

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
                finger_points = []            
                for i,lm in enumerate(hand_landmarks.landmark):
                    x = float(lm.x*w)
                    y = float(lm.y*h)

                    #print (i,x,y)

                    finger_points.append((x,y))

                if finger_points:
                    finger_angle = angle.hand_angle(finger_points) 
                    #print(finger_angle)                   
                    text = hand_pos(finger_angle)          
                    cv2.putText(img, str(text)+'F', (30,120), fontFace, 5, (255,255,255), 10, lineType) 

            floor.add(hand_pos(finger_angle))
            passtime += 1
            if passtime == 50:
                floor.remove(hand_pos(finger_angle))
                print("delete")
                cap.release()
                time.sleep(2)
                passtime = 0  
            if (0 in floor or None in floor):
                floor.discard(0)
                floor.discard(None)
                passtime = 0 

            if(chfloor != floor):
                chfloor = floor.copy()
                print(chfloor)
        else:
            passtime = 0          
        #print(passtime) 

        cv2.imshow('sx', img)
        if(not cap.isOpened()):
            cap = cv2.VideoCapture(0) 
        if cv2.waitKey(5) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()