from keras.models import load_model
from Game import Game
from State import State
from board import Board
from sklearn.preprocessing import StandardScaler
import joblib
class ComputerGameLogic(Game):
    def __init__(self):
        Game.__init__(self)
        self.model = load_model('avalon_model.h5')
        self.scaler = joblib.load('scaler.save')
    def changBoard(self, board):
        #פעולה שמקבלת לוח דו ממדי ומחזירה לוח חד ממדי מהסוג שנכנס לרשת ניורונים
        board1=[]
        for i in range (11):
            for j in range(11):
                if board.cells[i,j]==State.EMPTY:
                    board1+=[0]
                if board.cells[i,j]==State.BLACK:
                    board1+=[1]
                if board.cells[i,j]==State.WHITE:
                    board1+=[2]


        if board.turn == State.BLACK:
            board1+=[1]
        else:
            board1+=[2]
        return board1

    def boardAfterMove(self, board, move):
        saveBoard=board.board_to_string()
        saveBoard = "  " + saveBoard
        returnBoard = Board()
        returnBoard.string_to_board(saveBoard)
        returnBoard.make_a_move(move[0][0],move[0][1], move[1])
        return returnBoard

    def gradeBoards(self, possible_boards):
        possible_boards_scaled = self.scaler.transform(possible_boards)
        predictions = self.model.predict(possible_boards_scaled)
        return predictions

    def findBestGrade(self,grades):
        best_grade = -100
        best_grade_index = -1
        for i in range(len(grades)):
            if grades[i][0] > best_grade:
                best_grade_index= i
                best_grade = grades[i][0]
        return best_grade_index

    def smartMove(self, board):
        #פונקציה שמקבלת לוח ומחזירה את המהלך הטוב ביותר שהמחשב יעשה
        moves=board.all_ligel_moves()
        possible_boards = []
        for move in moves:
            possible_board = self.boardAfterMove(board, move)
            possible_boards += [self.changBoard(possible_board)]
        grades = self.gradeBoards(possible_boards)
        best_move_index = self.findBestGrade(grades)
        return moves[best_move_index]