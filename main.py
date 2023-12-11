from Graphics_Board import Graphics_Board
from Direction import *
import time
from board import *
visual_board = Graphics_Board()
board1 = Board()
board1.set_to_start()
board1.pr()
visual_board.set_to_start()

#
#
# #for i in range (4):
#     #for j in range (5+i):
#         #visual_board.draw_ball(5-i+j, i+1, "black")
#         #visual_board.draw_ball(j+1, 9-i, "white")
# ball=visual_board.draw_ball(5, 5, "white")
# ball2=visual_board.draw_ball(4,5,"white")
# ball3=visual_board.draw_ball(3,5,"white")
# ball4=visual_board.draw_ball(2,5, "black")
# ball5=visual_board.draw_ball(1,5, "black")
#
# mat = [ball,ball2,ball3]
# time.sleep(1)
#
# visual_board.move_balls(mat, Direction.RIGHT)
# time.sleep(1)
# visual_board.move_balls(mat, Direction.DOWN_RIGHT)
# time.sleep(1)
# visual_board.move_balls(mat, Direction.DOWN_LEFT)
# time.sleep(1)
# visual_board.move_balls(mat, Direction.LEFT)
# time.sleep(1)
# visual_board.move_balls(mat, Direction.UP_LEFT)
# time.sleep(1)
# visual_board.move_balls(mat, Direction.UP_RIGHT)
# time.sleep(1)
# visual_board.move_balls([ball,ball2,ball3,ball4,ball5], Direction.LEFT)
# visual_board.fall_ball(ball5)
# x1, y1, x2, y2= visual_board.wait_for_user_move()
# print(x1, y1, x2, y2)
x1, y1, x2, y2= visual_board.wait_for_user_move()
# # print(x1, y1, x2, y2)

