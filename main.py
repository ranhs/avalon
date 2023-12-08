from Graphics_Board import Graphics_Board
from Direction import *
visual_board = Graphics_Board()


#for i in range (4):
    #for j in range (5+i):
        #visual_board.draw_ball(5-i+j, i+1, "Red")
        #visual_board.draw_ball(j+1, 9-i, "Blue")
ball=visual_board.draw_ball(5, 5, "Pink")

visual_board.wait_for_mouse_click()
visual_board.move_ball(ball, Direction.RIGHT)
visual_board.wait_for_mouse_click()
visual_board.move_ball(ball, Direction.DOWN_RIGHT)
visual_board.wait_for_mouse_click()
visual_board.move_ball(ball, Direction.DOWN_LEFT)
visual_board.wait_for_mouse_click()
visual_board.move_ball(ball, Direction.LEFT)
visual_board.wait_for_mouse_click()
visual_board.move_ball(ball, Direction.UP_LEFT)
visual_board.wait_for_mouse_click()
visual_board.move_ball(ball, Direction.UP_RIGHT)

visual_board.wait_for_mouse_click()
