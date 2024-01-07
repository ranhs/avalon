from board import Board
from State import *
from Direction import  *
import random

class Game():
    def __init__(self):
        self.board = Board()
        self.board_scores = {}
        self.count = 0

    def scan_all_options(self, board, deep):
        self.count += 1
        if self.count % 100000 == 0:
           print(self.count)
        if deep <= 0:
            return
        moves = board.all_ligel_moves()
        for move in moves:
            fall, i, j =board.make_a_move(move[0][0],move[0][1],move[1])
            board.change_turn()
            self.scan_all_options(board,deep-1)
            board.make_a_move(i,j, Direction.OPPOSITE[move[1]])
            board.change_turn()



    def random_game(self):
        self.board = Board()
        self.board.set_to_start()
        win = False
        black_score = 0
        white_score = 0
        boards = []
        while not win:
            b = self.do_random_move()
            if b:
                if self.board.turn == State.WHITE:
                    black_score += 1
                    win = black_score >= 5
                else:
                    white_score += 1
                    win = white_score >= 5
            boards += [self.board.board_to_string()]
        print(self.board.turn, len(boards))
        print(black_score, white_score)
        self.board.pr()
        board_score = 0
        if black_score > white_score:
            board_score = -5000000
        else:
            board_score = 5000000
        boards.reverse()
        for board_str in boards:
            self.update_board_score(board_str, board_score)
            board_score *= 0.9
        #print(self.board_scores)

    def update_board_score(self, board_str, board_score):
        #value = self.board_scores[board_str]
        #if not value:
        #   value = (0,0)
        #value = ((value[0]*value[1]+board_score)/(value[1]+1),value[1]+1)
        #print("board_str", board_str)
        #self.board_scores["board_str"] = value
        print("update_board_core", board_str, board_score)


    def do_random_move(self):
        moves = self.board.all_ligel_moves()
        move_index = random.randrange(0,len(moves))
        selected_move = moves[move_index]
        b = self.board.make_a_move(selected_move[0][0],selected_move[0][1],selected_move[1])
        self.board.change_turn()
        return b

