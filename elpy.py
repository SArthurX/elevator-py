import cv2
import mediapipe as mp
from angle import hand_angle
from floor import  hand_pos
import time

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)            # 讀取攝影機
fontFace = cv2.FONT_HERSHEY_SIMPLEX  # 印出文字的字型
lineType = cv2.LINE_AA               # 印出文字的邊框

floor = set()
delfloor = set()
passtime = 0

# mediapipe 啟用偵測手掌
with mp_hands.Hands(
    max_num_hands=1,
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    while True:
        ret, img = cap.read()

        w,h = img.shape[1],img.shape[0]

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 轉換成 RGB 色彩
        results = hands.process(imgRGB)                # 偵測手勢
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                finger_points = []                   # 記錄手指節點座標的串列
                for i,lm in enumerate(hand_landmarks.landmark):
                    # 將 21 個節點換算成座標，記錄到 finger_points
                    x = float(lm.x*w)
                    y = float(lm.y*h)

                    #print (i,x,y)

                    finger_points.append((x,y))

                if finger_points:
                    finger_angle = hand_angle(finger_points) # 計算手指角度，回傳長度為 5 的串列
                    #print(finger_angle)                     # 印出角度 ( 有需要就開啟註解 )
                    text = hand_pos(finger_angle)            # 取得手勢所回傳的內容
                    cv2.putText(img, text, (30,120), fontFace, 5, (255,255,255), 10, lineType) # 印出文字

            floor.add(hand_pos(finger_angle))
            passtime += 1
            if passtime == 80:
                cv2.putText(img, "del", (30,120), fontFace, 5, (255,255,255), 10, lineType) # 印出文字
                delfloor.add(hand_pos(finger_angle))
                floor = floor.difference(delfloor)
                time.sleep(3)
                delfloor.clear()
                passtime = 0  
        else:
            passtime = 0             
        #print(passtime) 
        print(floor)      

        cv2.imshow('sx', img)
        if cv2.waitKey(5) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()