class State ():
    # מחלקה שמראה את המצב בו תא נמצא, חסום, ריק, שחוק לבן
    BLOCK=0
    EMPTY=1
    BLACK=2
    WHITE=3
    OTHER = [BLOCK,EMPTY,WHITE,BLACK] #נותן את ההופכי לצבע לפי מיקום
    EXIST = [False, False, True, True] #נותן האם יש כדור או לא לפי מיקום