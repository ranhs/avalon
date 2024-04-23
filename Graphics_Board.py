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
        self.drag_end = tkinter.IntVar()
        self.window = GraphWin("Avalon", 600, 600)
        self.window.bind('<Button-1>', self.mousedown)
        self.window.bind('<ButtonRelease-1>', self.mouseup)
        self.draw_board()
        print("L")
        self.balls = [None for i in range(11*11)]
        self.balls = np.array(self.balls).reshape((11, 11))
        self.blackScore = Text(Point(530, 490), "0")
        self.whiteScore = Text(Point(70, 490), "0")
        self.computer_play = False
    def prv(self):
        #מדפיס את האוביקטים של הלוח הגרפי
        for j in range(11):
            for i in range(11):
                print(self.balls[i,j], end=' ')
            print()


    def mousedown(self,event):
        #מחזיר את המקום שבו נלחץ העכבר
        self.x_drag_start,self.y_drag_start = event.x, event.y

    def mouseup(self,event):
        #מחזיר את המקום שעוזבים בו את העכבר
        self.x_drag_end,self.y_drag_end = event.x, event.y
        self.drag_end.set(1)

    def view_to_model(self, x, y):
        #מקבל מיקומים על המסך ומחזיר לאינדקסים של כדור במודל
        j = (y / radius - 1.7) / line
        i = (x / radius + 4.5 - j * 1.1) / 2.2
        return i, j
    def wait_for_user_move(self):
        #מחזיר את האינקסים של כדור במודל בעקבות לחיצה וגרירה של המשתמש
        self.window.wait_variable(self.drag_end)
        i1, j1 = self.view_to_model(self.x_drag_start, self.y_drag_start)
        i2, j2 = self.view_to_model( self.x_drag_end, self.y_drag_end)
        return int(round(i1,0)),int(round(j1,0)), int(round(i2,0)),int(round(j2,0))
    def draw_board(self):
        #מייצר מסך ריק ולוח משושה של המודל
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
        #מייצר ומחזיר אוביקט של כדור אחד
        if self.balls is None or self.balls[i,j] is None:
            c = Circle(Point(radius *(2.2 * i +1.1 *j-4.5), radius * (1.7+line*j)), r)
            c.setFill(color)
            if self.balls is not None:
                self.balls[i,j] = c
            c.draw(self.window)
            return c
    def move_balls_internal(self, balls, delta_x, delta_y):
        #מזיז את הכדורים לפי המשתמש בצורה גרפית
        for i in range(22):
            for ball in balls:
                ball.move(delta_x, delta_y)
            time.sleep(0.05)
    def fall_ball(self, ball):
        #עושד אנימציה של הפלת כדור
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
        #מזיז כדור במערך של אוביקט הכדורים
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
        #מאתחל את הלוח הגרפי ומייצר את הכדורים
        super().set_to_start()
        for i in range(11):
            for j in range(11):
                if self.cells[i, j] == State.WHITE:
                    self.draw_ball(i,j, "white")
                if self.cells[i, j] == State.BLACK:
                    self.draw_ball(i,j, "black")
        self.graphic_count()

    def graphic_count(self):
        # מדפיס את הכותרות של ספירת הנקודות
        message = Text(Point(530, 450), "black")
        message.setSize(18)
        message.setStyle("bold")
        message.draw(self.window)
        self.blackScore.setText("0")
        self.blackScore.setSize(18)
        self.blackScore.setStyle("bold")
        self.blackScore.draw(self.window)
        message1 = Text(Point(70, 450), "white")
        message1.setSize(18)
        message1.setStyle("bold")
        message1.draw(self.window)
        self.whiteScore.setText("0")
        self.whiteScore.setSize(18)
        self.whiteScore.setStyle("bold")
        self.whiteScore.draw(self.window)



    def draw_count(self,n, color):
        print("...inside draw_count", n, color)
        #מדפיס את המספר של הניקוד
        if color==State.BLACK:
            self.blackScore.setText(n)
        if color == State.WHITE:
            self.whiteScore.setText(n)

    def win(self):
        #מדפיס מסך ניצחון
        if self.count_black == 5:
            message = Text(Point(300, 200), "BLACK WON!")
            message.setSize(35)
            message.setTextColor("red")
            message.setStyle("bold")
            message.setFace("helvetica")
            message.draw(self.window)
            return True
        if self.count_white == 5:
            message = Text(Point(300, 200), "WHITE WON!")
            message.setSize(35)
            message.setTextColor("red")
            message.setStyle("bold")
            message.setFace("helvetica")
            message.draw(self.window)
            return True
        return False


    def make_a_turn(self, x1 ,y1 ,d):
        #עושה את כל הפעולה של התור כולל עדוכנים ובדיקה של תור
        own, other, next, row = self.how_much_in_a_row(x1, y1, d)
        if self.is_OK(x1, y1, d):
            balls = []
            for ball in row:
                b = self.balls[ball]
                balls += [b]
            row.reverse()
            self.move_balls(balls, d)
            for ball in row:
                x= ball[0]
                y= ball[1]
                n1,n2 =self.next_in_direction(x,y,d)
                if self.cells[n1,n2] == State.BLOCK:
                    self.fall_ball(self.balls[x,y])
                    x = self.count_up(x,y)
                    print("calling draw_count", x, self.turn)
                    self.draw_count(x, self.turn)
                else:
                    self.cells[n1,n2] = self.cells[x,y]
                    self.balls[n1,n2] = self.balls[x,y]
            self.cells[x1, y1] = State.EMPTY
            self.balls [x1, y1] = None
            self.change_turn()
            return self.win()
        return False

    def open_Screen(self):
        rec = Rectangle(Point(0,0), Point(1000,1000))
        rec.setFill("white")
        rec.setOutline("white")
        rec.draw(self.window)
        text1 = Text(Point(300, 170), "Welcome to\nAvalon")
        text1.setSize(35)
        text1.setTextColor("blue")
        text1.setStyle("bold")
        text1.setFace("helvetica")
        text1.draw(self.window)
        rec1 = Rectangle(Point(90,300), Point(290,500))
        rec1.setFill("white")
        rec1.setOutline("blue")
        rec1.draw(self.window)
        rec2 = Rectangle(Point(310,300), Point(510,500))
        rec2.setFill("white")
        rec2.setOutline("blue")
        rec2.draw(self.window)
        text2 = Text(Point(190, 400), "Human\nvs.\nHuman")
        text2.setSize(25)
        text2.setTextColor("blue")
        text2.setStyle("bold")
        text2.setFace("helvetica")
        text2.draw(self.window)
        text3 = Text(Point(410, 400), "Human\nvs.\nComputer")
        text3.setSize(25)
        text3.setTextColor("blue")
        text3.setStyle("bold")
        text3.setFace("helvetica")
        text3.draw(self.window)
        while True:
            self.window.wait_variable(self.drag_end)
            print(self.x_drag_end, self.y_drag_end)
            if self.y_drag_end<300 or self.y_drag_end>500:
                continue
            if self.x_drag_end>=90 and self.x_drag_end<=290:
                self.computer_play = False
                break
            if self.x_drag_end >= 310 and self.x_drag_end <= 510:
                self.computer_play = True
                break
        rec.undraw()
        rec1.undraw()
        rec2.undraw()
        text1.undraw()
        text2.undraw()
        text3.undraw()
def wait_for_mouse_click(self):
    #מחכה ללחיצה של משתמש ומדפיס את המיקום שבו הוא לחץ
    rv = self.window.getMouse()
    print(rv)
