from Graphics_Board import Graphics_Board
from Direction import *
import time
visual_board = Graphics_Board()


#for i in range (4):
    #for j in range (5+i):
        #visual_board.draw_ball(5-i+j, i+1, "Red")
        #visual_board.draw_ball(j+1, 9-i, "Blue")
ball=visual_board.draw_ball(5, 5, "Pink")
ball2=visual_board.draw_ball(4,5,"pink")
ball3=visual_board.draw_ball(3,5,"pink")
mat = [ball,ball2,ball3]
time.sleep(1)

visual_board.move_balls(mat, Direction.RIGHT)
time.sleep(1)
visual_board.move_balls(mat, Direction.DOWN_RIGHT)
time.sleep(1)
visual_board.move_balls(mat, Direction.DOWN_LEFT)
time.sleep(1)
visual_board.move_balls(mat, Direction.LEFT)
time.sleep(1)
visual_board.move_balls(mat, Direction.UP_LEFT)
time.sleep(1)
visual_board.move_balls(mat, Direction.UP_RIGHT)

x1, y1, x2, y2= visual_board.wait_for_user_move()
print(x1, y1, x2, y2)
x1, y1, x2, y2= visual_board.wait_for_user_move()
print(x1, y1, x2, y2)
