def hand_pos(finger_angle):
    f1 = finger_angle[0]   # 大拇指角度
    f2 = finger_angle[1]   # 食指角度
    f3 = finger_angle[2]   # 中指角度
    f4 = finger_angle[3]   # 無名指角度
    f5 = finger_angle[4]   # 小拇指角度

    # 小於 50 表示手指伸直，大於等於 50 表示手指捲縮
    if f1<50 and f2>=50 and f3>=50 and f4>=50 and f5>=50:
        return 'good'
    #elif f1>=50 and f2>=50 and f3<50 and f4>=50 and f5>=50:
    #    return 'no!!!'
    #elif f1<50 and f2<50 and f3>=50 and f4>=50 and f5<50:
    #    return 'ROCK!'
    elif f1>=50 and f2>=50 and f3>=50 and f4>=50 and f5>=50:
        return '0'
    #elif f1>=50 and f2>=50 and f3>=50 and f4>=50 and f5<50:
    #    return 'pink'
    elif f1>=50 and f2<50 and f3>=50 and f4>=50 and f5>=50:
        return '1F'
    elif f1>=50 and f2<50 and f3<50 and f4>=50 and f5>=50:
        return '2F'
    #elif f1>=50 and f2>=50 and f3<50 and f4<50 and f5<50:
    #    return 'ok'
    #elif f1<50 and f2>=50 and f3<50 and f4<50 and f5<50:
    #    return 'ok'
    elif f1>=50 and f2<50 and f3<50 and f4<50 and f5>50:
        return '3F'
    elif f1>=50 and f2<50 and f3<50 and f4<50 and f5<50:
        return '4F'
    elif f1<50 and f2<50 and f3<50 and f4<50 and f5<50:
        return '5F'
    elif f1<50 and f2>=50 and f3>=50 and f4>=50 and f5<50:
        return '6F'
    elif f1<50 and f2<50 and f3>=50 and f4>=50 and f5>=50:
        return '7F'
    elif f1<50 and f2<50 and f3<50 and f4>=50 and f5>=50:
        return '8F'
    elif f1<50 and f2<50 and f3<50 and f4<50 and f5>=50:
        return '9F'
    #else:
    #    return ''
# 根據手指角度的串列內容，返回對應的手勢名稱