from Graphics_Board import Graphics_Board
from Game import *
from Direction import *
import time
from board import *
#board1 = visual_board = Graphics_Board()
#print("X1")
#visual_board.set_to_start()
#visual_board.pr()
#print()
#visual_board.prv()
game =Game()
game.random_game()

#
#
# #for i in range (4):
#     #for j in range (5+i):
#         #visual_board.draw_ball(5-i+j, i+1, "black")
#         #visual_board.draw_ball(j+1, 9-i, "white")
#ball=visual_board.draw_ball(7, 5, "white")
#ball2=visual_board.draw_ball(6,5,"white")
#ball3=visual_board.draw_ball(5,5,"white")
#ball4=visual_board.draw_ball(4,5, "black")
#ball5=visual_board.draw_ball(3,5, "white")
#board1.add_balls()
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
#print(x1, y1, x2, y2)



# while True:
#     board1.board_to_string()
#     board1.all_ligel_moves()
#     x1, y1, x2, y2= visual_board.wait_for_user_move()
#     print(x1, y1, x2, y2)
#     d = board1.which_direction(x1, y1, x2, y2)
#     print(d)
#     if d == None:
#         continue
#     print(board1.next_in_direction(x1,y1, d))
#     own, other, n, row= board1.how_much_in_a_row(x1, y1, d)
#     print(own, other, n, row)
#     ok = board1.is_OK(x1,y1,d)
#     print(ok)
#     board1.all_ligel_moves()
#     # if ok:
#     #     balls = []
#     #     for ball in row:
#     #         b = visual_board.balls[ball]
#     #         balls += [b]
#     #     print(balls, d)
#     #     visual_board.move_balls(balls,d)
#     if ok:
#         visual_board.make_a_turn(x1, y1, d)
#     board1.pr()
