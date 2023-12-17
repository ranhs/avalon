from graphics import *
from Direction import *
import time
import tkinter
from board import *
from threading import Event
import numpy as np
line=1.9052
radius = 25
class Graphics_Board(Board):
    def __init__(self):
        self.balls = None
        Board.__init__(self)
        self.x_drag_start = 0
        self.y_drag_start = 0
        self.x_drag_end = 0
        self.y_drag_end = 0
        self.count_black=0
        self.count_white=0
        self.drag_end = tkinter.IntVar()
        self.window = GraphWin("Avalon", 600, 600)
        self.window.bind('<Button-1>', self.mousedown)
        self.window.bind('<ButtonRelease-1>', self.mouseup)
        self.draw_board()
        print("L")
        self.balls = [None for i in range(11*11)]
        self.balls = np.array(self.balls).reshape((11, 11))
    def prv(self):
        for j in range(11):
            for i in range(11):
                print(self.balls[i,j], end=' ')
            print()


    def mousedown(self,event):
        self.x_drag_start,self.y_drag_start = event.x, event.y

    def mouseup(self,event):
        self.x_drag_end,self.y_drag_end = event.x, event.y
        self.drag_end.set(1)

    def view_to_model(self, x, y):
        j = (y / radius - 1.7) / line
        i = (x / radius + 4.5 - j * 1.1) / 2.2
        return i, j
    def wait_for_user_move(self):
        self.window.wait_variable(self.drag_end)
        i1, j1 = self.view_to_model(self.x_drag_start, self.y_drag_start)
        i2, j2 = self.view_to_model( self.x_drag_end, self.y_drag_end)
        return int(round(i1,0)),int(round(j1,0)), int(round(i2,0)),int(round(j2,0))
    def draw_board(self):
        self.window.setBackground("white")
        p1=Point (int(6.85*radius), int(2.3*radius))
        p2=Point( int(17.15*radius), int(2.3*radius))
        p3=Point (int(22.3*radius), int(11.22*radius))
        p4=  Point( int(17.15*radius), int(20.14 *radius))
        p5=Point (int(6.85*radius), int(20.14*radius))
        p6=Point (int(1.7*radius), int(11.22*radius))
        aPolygon = Polygon(p1, p2, p3, p4, p5, p6)
        aPolygon.draw(self.window)
        aPolygon.setFill("gray")

        for i in range(5):
            for j in range(5 + i):
                self.draw_ball(5 - i + j, i + 1, "light gray", radius)
                self.draw_ball(j + 1, 9 - i, "light gray", radius)
                self.draw_ball(5 - i + j, i + 1, "gray", radius*0.7)
                self.draw_ball(j + 1, 9 - i, "gray", radius*0.7)

    def draw_ball(self, i, j, color, r = radius):
        if self.balls is None or self.balls[i,j] is None:
            c = Circle(Point(radius *(2.2 * i +1.1 *j-4.5), radius * (1.7+line*j)), r)
            c.setFill(color)
            if self.balls is not None:
                self.balls[i,j] = c
            c.draw(self.window)
            return c
    def move_balls_internal(self, balls, delta_x, delta_y):
        for i in range(22):
            for ball in balls:
                ball.move(delta_x, delta_y)
            time.sleep(0.05)
    def fall_ball(self, ball):
        ball.undraw()
        center = ball.getCenter()
        fill = ball.config['fill']
        for i in range(15):
            c= Circle (center, int(radius/15*(15-i)) )
            c.setFill(fill)
            c.draw(self.window)
            time.sleep(0.05)
            c.undraw()




    def move_balls(self, balls, dir):
        if dir==Direction.RIGHT:
            self.move_balls_internal(balls, radius*0.1, 0)
        elif dir==Direction.LEFT:
            self.move_balls_internal(balls, -radius*0.1, 0)
        elif dir == Direction.UP_LEFT:
            self.move_balls_internal(balls, -radius * 0.05, -radius*line/22)
        elif dir == Direction.UP_RIGHT:
            self.move_balls_internal(balls, radius * 0.05, -radius * line/22)
        elif dir == Direction.DOWN_RIGHT:
            self.move_balls_internal(balls, radius*0.05, radius * line/22)
        elif dir == Direction.DOWN_LEFT:
            self.move_balls_internal(balls, -radius*0.05, radius * line/22)
    def set_to_start(self):
        super().set_to_start()
        for i in range(11):
            for j in range(11):
                if self.cells[i, j] == State.WHITE:
                    self.draw_ball(i,j, "white")
                if self.cells[i, j] == State.BLACK:
                    self.draw_ball(i,j, "black")

    def count_up(self,x,y):
        if self.cells[x,y] == State.BLACK:
            self.count_white+=1
        else:
            self.count_black+=1
    def win(self):
        if self.count_black == 5:
            message = Text(Point(3, 4), "Black won")
        if self.count_white == 5:
            message = Text(Point(3, 4), "White won")


    def make_a_turn(self, x1 ,y1 ,d):
        own, other, next, row = self.how_much_in_a_row(x1, y1, d)
        if self.is_OK(x1, y1, d):
            balls = []
            for ball in row:
                b = self.balls[ball]
                balls += [b]

            print(row)
            row.reverse()
            print(row)
            self.move_balls(balls, d)
            for ball in row:
                x= ball[0]
                y= ball[1]
                n1,n2 =self.next_in_direction(x,y,d)
                if self.cells[n1,n2] == State.BLOCK:
                    self.fall_ball(self.balls[x,y])

                else:
                    self.cells[n1,n2] = self.cells[x,y]
                    self.balls[n1,n2] = self.balls[x,y]
            self.cells[x1, y1] = State.EMPTY
            self.balls [x1, y1] = None
            self.change_turn()


def wait_for_mouse_click(self):
    rv = self.window.getMouse()
    print(rv)