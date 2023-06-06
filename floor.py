def hand_pos(finger_angle):
    f1 = finger_angle[0]   
    f2 = finger_angle[1]   
    f3 = finger_angle[2]   
    f4 = finger_angle[3]   
    f5 = finger_angle[4]   

    if f1>=50 and f2>=50 and f3>=50 and f4>=50 and f5>=50:
        return 0
    elif f1>=50 and f2<50 and f3>=50 and f4>=50 and f5>=50:
        return 1
    elif f1>=50 and f2<50 and f3<50 and f4>=50 and f5>=50:
        return 2
    elif f1>=50 and f2<50 and f3<50 and f4<50 and f5>50:
        return 3
    elif f1>=50 and f2<50 and f3<50 and f4<50 and f5<50:
        return 4
    elif f1<50 and f2<50 and f3<50 and f4<50 and f5<50:
        return 5
    elif f1<50 and f2>=50 and f3>=50 and f4>=50 and f5<50:
        return 6
    elif f1<50 and f2<50 and f3>=50 and f4>=50 and f5>=50:
        return 7
    elif f1<50 and f2<50 and f3<50 and f4>=50 and f5>=50:
        return 8
    elif f1<50 and f2<50 and f3<50 and f4<50 and f5>=50:
        return 9
    elif f1>=50 and f2>=50 and f3<50 and f4>=50 and f5>=50:
        return 44
    #elif f1<50 and f2<50 and f3>=50 and f4>=50 and f5<50:
    #    return 69 #open
    #elif f1>=50 and f2<50 and f3>=50 and f4>=50 and f5<50:
    #    return 96 #close
    #elif f1<50 and f2>=50 and f3>=50 and f4>=50 and f5>=50:
    #    return 12 #

    #elif f1>=50 and f2>=50 and f3<50 and f4<50 and f5<50:
    #    return 'ok'
    #elif f1<50 and f2>=50 and f3<50 and f4<50 and f5<50:
    #    return 'ok'
    #elif f1>=50 and f2>=50 and f3>=50 and f4>=50 and f5<50:
    #    return 'pink'
    #else:
    #    return ''