from graphics import *
from Direction import *
line=1.9052
radius = 25
class Graphics_Board:
    def __init__(self):
        self.window = GraphWin("Avalon", 600, 600)
        self.draw_board()
    def draw_board(self):
        self.window.setBackground("Black")
        for i in range(5):
            for j in range(5 + i):
                self.draw_ball(5 - i + j, i + 1, "Gray", radius)
                self.draw_ball(j + 1, 9 - i, "Gray", radius)
                self.draw_ball(5 - i + j, i + 1, "Black", radius*0.7)
                self.draw_ball(j + 1, 9 - i, "Black", radius*0.7)


    def draw_ball(self, i, j, color, r = radius):
        c = Circle(Point(radius *(2.2 * i +1.1 *j-4.5), radius * (1.7+line*j)), r)
        c.setFill(color)
        c.draw(self.window)
        return c
    def move_ball(self, ball, dir):
        if dir==Direction.RIGHT:
            ball.move(radius*2.2, 0)
        elif dir==Direction.LEFT:
            ball.move(-radius*2.2, 0)
        elif dir == Direction.UP_LEFT:
            ball.move(-radius*1.1, -radius*line)
        elif dir == Direction.UP_RIGHT:
            ball.move(radius*1.1, -radius * line)
        elif dir == Direction.DOWN_RIGHT:
            ball.move(radius*1.1, radius * line)
        elif dir == Direction.DOWN_LEFT:
            ball.move(-radius*1.1, radius * line)




    def wait_for_mouse_click(self):
        self.window.getMouse()