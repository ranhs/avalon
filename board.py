from State import *
import numpy as np

class Board():
    def __init__(self):
        self.cells = [int for i in range(11*11)]
        self.cells = np.array(self.cells).reshape((11, 11))
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

