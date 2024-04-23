from Graphics_Board import Graphics_Board
from Game import *
from Direction import *
import time
from board import *
from datetime import datetime
from ComputerGameLogic import ComputerGameLogic

computer = ComputerGameLogic()
board1 = visual_board = Graphics_Board()
print("X1")
visual_board.set_to_start()
visual_board.pr()
print()
visual_board.prv()
#################################
#game =Game()
#print('game', game)
# game.random_game()
#################################
board = Board()
board.set_to_start()
board.pr()
#x,y=game.until_a_ball_fall(board.board_to_string())
#print(x,y)


#now = datetime.now()
#current_time = now.strftime("%H:%M:%S")
#print("Current Time =", current_time)
#file = open('avalonscores.json','r')
#data = file.read()
#file.close()
#game.board_scores = json.loads(data)
#for i in range(1000):
#   game.random_game(i)
#now = datetime.now()
#current_time = now.strftime("%H:%M:%S")
#print("Current Time =", current_time)
#
# print('before')
# x,y=game.scan_all_options(board,4)
# print(game.count)
# print(x,y)
# print('after')

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

visual_board.open_Screen()

while True:
    #board1.board_to_string()
    #board1.all_ligel_moves()
    print("turn = ", board1.turn)
    if board1.turn == State.BLACK or not visual_board.computer_play:
        x1, y1, x2, y2= visual_board.wait_for_user_move()
        print(x1, y1, x2, y2)
        d = board1.which_direction(x1, y1, x2, y2)
        print(d)
        if d == None:
            continue
    else:
        move = computer.smartMove(board1)
        x1 = move[0][0]
        y1 = move[0][1]
        d = move[1]
    print(board1.next_in_direction(x1,y1, d))
    own, other, n, row= board1.how_much_in_a_row(x1, y1, d)
    print(own, other, n, row)
    ok = board1.is_OK(x1,y1,d)
    print(ok)
    #board1.all_ligel_moves()
    # if ok:
    #     balls = []
    #     for ball in row:
    #         b = visual_board.balls[ball]
    #         balls += [b]
    #     print(balls, d)
    #     visual_board.move_balls(balls,d)
    if ok:
        has_winner = visual_board.make_a_turn(x1, y1, d)
        if has_winner:
            break
    board1.pr()
visual_board.wait_for_user_move()