from graphics import *
from Direction import *
import time
import tkinter
from threading import Event
import numpy as np
line=1.9052
radius = 25
class Graphics_Board:
    def __init__(self):
        self.x_drag_start = 0
        self.y_drag_start = 0
        self.x_drag_end = 0
        self.y_drag_end = 0
        self.drag_end = tkinter.IntVar()
        self.window = GraphWin("Avalon", 600, 600)
        self.window.bind('<Button-1>', self.mousedown)
        self.window.bind('<ButtonRelease-1>', self.mouseup)
        self.draw_board()

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
        return round(i1,0) ,round(j1,0) ,round(i2,0) ,round(j2,0)
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
    def move_balls_internal(self, balls, delta_x, delta_y):
        for i in range(22):
            for ball in balls:
                ball.move(delta_x, delta_y)
            time.sleep(0.05)

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




def wait_for_mouse_click(self):
    rv = self.window.getMouse()
    print(rv)