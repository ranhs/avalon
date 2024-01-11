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
        count_black=10000
        count_white=10000
        self.count += 1
        if self.count % 100000 == 0:
           print(self.count)
        if deep <= 0:
            return count_black,count_white
        moves = board.all_ligel_moves()
        for move in moves:
            fall, i, j =board.make_a_move(move[0][0],move[0][1],move[1])
            board.change_turn()
            if fall == False:
                b,w= self.scan_all_options(board,deep-1)
                if b<count_black:
                    count_black=b+1
                if w<count_white:
                    count_white=b+1
            value = self.board_scores.get(board.board_to_string())
            board.make_a_move(i,j, Direction.OPPOSITE[move[1]])
            if fall:
                i,j=board.next_in_direction(i,j,Direction.OPPOSITE[move[1]])
                board.cells[i][j] = board.turn
                if board.turn == State.BLACK:
                    count_white=1
                else:
                    count_black=1
            board.change_turn()
        if value != None:
            if value.b < count_black:
                count_black = value.b
            if value.w < count_white:
                count_white = value.w
        return count_black,count_white



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
            boards.append(chr(black_score+48)+chr(white_score+48)+ self.board.board_to_string())
        print(self.board.turn, len(boards))
        print(black_score, white_score)
        boards.reverse()
        for board_str in boards:
            self.board_score(board_str)
            print(board_str, self.board_scores.get(board_str))
        print(self.board_scores)

    def do_random_move(self):
        moves = self.board.all_ligel_moves()
        move_index = random.randrange(0,len(moves))
        selected_move = moves[move_index]
        b, i,j = self.board.make_a_move(selected_move[0][0],selected_move[0][1],selected_move[1])
        self.board.change_turn()
        return b

    def board_score(self, board_str):
        score_b=int(board_str[0])
        score_w=int(board_str[1])
        if score_b==5:
            self.board_scores[board_str] = {"b":10000, "w":10000, "s":-1}
            return
        if score_w==5:
            self.board_scores[board_str] = {"b":10000, "w":10000, "s":1}
            return
        value=self.board_scores.get(board_str)
        if not value:
            value = {"b":10000,"w":10000,"s":0}

        board=Board()
        board.string_to_board(board_str)
        self.count = 0
        b,w=self.scan_all_options(board,4)
        if b<value["b"]:
            value["b"]=b
        if w<value["w"]:
            value["w"]=w
        if value["b"]<10000:
            score_b += pow(0.9,value["b"])
        if value["w"]<10000:
            score_w += pow(0.9,value["w"])
        s = ((5-score_b)-(5-score_w))/max(5-score_w,5-score_b)
        value["s"] = s
        self.board_scores[board_str] = value