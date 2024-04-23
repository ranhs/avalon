
class Direction():
    # ערכים שמציינים כיוון תזוזה של כדור
    LEFT =1
    RIGHT=2
    UP_LEFT=3
    UP_RIGHT=4
    DOWN_LEFT=5
    DOWN_RIGHT=6
    OPPOSITE = [0, RIGHT, LEFT, DOWN_RIGHT, DOWN_LEFT, UP_RIGHT, UP_LEFT]
    NEXT_IN_DIRECTION = [(0,0),(-1, 0), (1, 0), (0,-1), (1,-1), (-1, 1), (0,1)]