def update_hand_pos(gesture_data):
    with open("hand.py", "a") as file:  # 使用 'a' 模式以附加方式打開檔案
        for idx, gesture in gesture_data.items():
            for i,x in enumerate (gesture):
                if x == 0:
                    gesture[i]=">"
                elif x == 1:
                    gesture[i]="<"
            gesture_values = " ".join(map(str, gesture))
            file.write(f"    elif f1 {gesture[0]} 50 and f2 {gesture[1]} 50 and f3 {gesture[2]} 50 and f4 {gesture[3]} 50 and f5 {gesture[4]} 50:\n")
            file.write(f"        return {idx}\n")

def hand_pos(finger_angle):
    f1 = finger_angle[0]
    f2 = finger_angle[1]
    f3 = finger_angle[2]
    f4 = finger_angle[3]
    f5 = finger_angle[4]

    if f1 >= 50 and f2 >= 50 and f3 >= 50 and f4 >= 50 and f5 >= 50:
        return 0
    elif f1 >= 50 and f2 < 50 and f3 >= 50 and f4 >= 50 and f5 >= 50:
        return 1
    elif f1 >= 50 and f2 < 50 and f3 < 50 and f4 >= 50 and f5 >= 50:
        return 2
    elif f1 >= 50 and f2 < 50 and f3 < 50 and f4 < 50 and f5 > 50:
        return 3
    elif f1 >= 50 and f2 < 50 and f3 < 50 and f4 < 50 and f5 < 50:
        return 4
    elif f1 < 50 and f2 < 50 and f3 < 50 and f4 < 50 and f5 < 50:
        return 5
    elif f1 < 50 and f2 >= 50 and f3 >= 50 and f4 >= 50 and f5 < 50:
        return 6
    elif f1 < 50 and f2 < 50 and f3 >= 50 and f4 >= 50 and f5 >= 50:
        return 7
    elif f1 < 50 and f2 < 50 and f3 < 50 and f4 >= 50 and f5 >= 50:
        return 8
    elif f1 < 50 and f2 < 50 and f3 < 50 and f4 < 50 and f5 >= 50:
        return 9
    elif f1 >= 50 and f2 >= 50 and f3 < 50 and f4 >= 50 and f5 >= 50:
        return 44
    elif f1 <= 50 and f2 <= 50 and f3 >= 50 and f4 >= 50 and f5 <= 50:
        return 101
