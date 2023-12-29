from Move import Move
from State import *
import numpy as np
from Direction import *
class Board():
    def __init__(self):
        self.turn = State.BLACK
        self.cells = [int for i in range(11*11)]
        self.cells = np.array(self.cells).reshape((11, 11))
        self.count_white=0
        self.count_black=0
        for i in range(11):
            for j in range(11):
                if i == 0 or i == 10 or j == 0 or j == 10 or i+j < 6 or i+j > 14:
                    self.cells[i][j] = State.BLOCK
                else:
                    self.cells[i , j] = State.EMPTY

    def pr(self):
        for j in range(11):
            for i in range(11):
                print(self.cells[i,j].value, end=' ')
            print()


    def set_to_start(self):
        for i in range(11):
            for j in range(11):
                if j == 1 or j == 2 or j == 3 and i >= 5 and i <= 7:
                    if self.cells[i,j] == State.EMPTY:
                        self.cells[i][j] = State.WHITE
                if j == 8 or j == 9 or j == 7 and i >= 3 and i <= 5:
                    if self.cells[i,j] == State.EMPTY:
                        self.cells[i][j] = State.BLACK
    def is_a_ball(self, x, y):
        if self.cells[x,y] == State.WHITE or self.cells[x,y] == State.BLACK:
            return True
        else:
            return False

    def legal_index(self,x1, y1, x2, y2):
        if abs(x1-x2)>1 or abs(y1-y2)>1:
            return False
        if x1 == x2 and y1 == y2:
            return False
        if (x1-x2)*(y1-y2)>0:
            return False
        return True
    def which_direction(self, col1, row1, col2, row2):
        if self.legal_index(col1, row1, col2, row2) == False:
            return None
        if row1 == row2:
            if col1-col2 == 1:
                return Direction.LEFT
            if col1 - col2 == -1:
                return Direction.RIGHT
        if col1 == col2:
            if row1 - row2 == 1:
                return Direction.UP_LEFT
            if row1 - row2 == -1:
                return Direction.DOWN_RIGHT

        if row1-row2 ==1 and col1-col2 ==-1:
            return Direction.UP_RIGHT
        if row1-row2 ==-1 and col1-col2 ==1:
            return Direction.DOWN_LEFT
        return None
    def next_in_direction(self,col , row, d):
        if d == Direction.RIGHT:
            return col + 1, row
        if d == Direction.LEFT:
            return col - 1, row
        if d == Direction.UP_RIGHT:
            return col + 1, row - 1
        if d == Direction.DOWN_RIGHT:
            return col, row + 1
        if d==Direction.UP_LEFT:
            return col,row - 1
        if d == Direction.DOWN_LEFT:
            return col - 1,row + 1
    def change_turn(self):
        if self.turn == State.BLACK:
            self.turn = State.WHITE
        else:
            self.turn = State.BLACK

    def how_much_in_a_row(self,x,y,d):
        count_own=0
        count_other =0
        row = []
        color = self.cells[x,y]
        while self.cells[x,y]!= State.EMPTY and self.cells[x,y]!= State.BLOCK and self.cells[x,y] == color:
            count_own+=1
            row += [(x,y)]
            x,y=self.next_in_direction(x,y,d)
        while self.cells[x,y]!= State.EMPTY and self.cells[x,y]!= State.BLOCK and self.cells[x,y] != color:
            count_other+=1
            row += [(x,y)]
            x,y=self.next_in_direction(x,y,d)
        next = self.cells[x,y]
        return count_own,count_other, next, row

    def count_up(self, x, y):
        if self.cells[x, y] == State.BLACK:
            self.count_white += 1
            return self.count_white
        else:
            self.count_black += 1
            return self.count_black
    def is_OK(self,x, y, d):

        if self.turn != self.cells[x,y]:
            return False
        count_own, count_other, next, row = self.how_much_in_a_row(x,y,d)
        if count_own == 1 and count_other == 0 and next == State.EMPTY:
                return True
        if count_own > 0 and count_other == 0 and next == State.BLOCK:
            return False
        if count_own > count_other and count_own <=3:
            if next == State.EMPTY or next == State.BLOCK:
                return True
        return False
    def make_a_move(self, i, j, d):
        i1, j1 = self.next_in_direction(i,j,d)
        if self.cells[i1,j1] == State.EMPTY:
            self.cells[i1,j1] = self.cells[i,j]
            self.cells[i,j] = State.EMPTY
            return False
        if self.cells[i1,j1] == State.BLOCK:
            self.cells[i,j] = State.EMPTY
            return True
        b = self.make_a_move(i1,j1,d)
        self.cells[i1, j1] = self.cells[i, j]
        self.cells[i, j] = State.EMPTY
        return b

    def all_ligel_moves(self):
        moves = []
        for j in range(11):
            for i in range(11):
                if self.cells[i,j]==self.turn:
                    if self.is_OK(i, j, Direction.RIGHT):
                        moves.append(((i, j), Direction.RIGHT))
                    if self.is_OK(i, j, Direction.LEFT):
                        moves.append(((i,j),Direction.LEFT))
                    if self.is_OK(i, j, Direction.UP_LEFT):
                        moves.append(((i,j),Direction.UP_LEFT))
                    if self.is_OK(i, j, Direction.UP_RIGHT):
                        moves.append(((i, j), Direction.UP_RIGHT))
                    if self.is_OK(i, j, Direction.DOWN_LEFT):
                        moves.append(((i, j), Direction.DOWN_LEFT))
                    if self.is_OK(i, j, Direction.DOWN_RIGHT):
                        moves.append(((i, j), Direction.DOWN_RIGHT))


        return moves


    def board_to_string(self):
        bstr = ""
        wstr = ""
        bcount = 0
        wcount = 0
        for j in range(11):
            for i in range(11):
                if self.cells[i,j] == State.BLOCK:
                    continue
                if self.cells[i,j] == State.BLACK:
                    bstr += chr(bcount+48)
                    bcount = 0
                if self.cells[i,j] == State.WHITE:
                    wstr += chr(wcount+48)
                    wcount = 0
                bcount += 1
                wcount += 1
        turn = "@"
        if self.turn == State.BLACK:
            turn = "#"
        code = bstr+turn+wstr
        return code

