from board import Board
from State import *
from Direction import  *
import random
import json

class Game(Board):
    def __init__(self):
        Board.__init__(self)
        self.board = Board()
        self.board_scores = {}
        self.count = 0

    def scan_all_options(self, board, deep):
        # not used method
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


    def until_a_ball_fall(self, board_str):
        # הרצת 200 משחקים אקראיים ממצב לוח נתון עד נפילת הכדור הבאה
        # תוך כדי הריצות סופרים כמה מהלכים משוחקים עד נפילת הכדור הלבן או השחור
        # הפונקציה מחזירה את המספר המהליכים המינימלי עד נפילת כדור שחור ועד נפילת כדור לבן
        # המטרה לקבל אומדן טוב למינימום האמיתי לאחר הרצת מספר גדול של משחקים
        minB= 10000
        minW=10000
        for i in range(200):
            board1 = Board()
            board1.string_to_board(board_str)
            count,color= self.random_until_fall(board1, max(minW,minB))
            if color != None:
                if minW>count and color==State.WHITE:
                    minW=count
                if minB > count and color == State.BLACK:
                    minB = count
        return minB,minW
    def random_game(self,i):
        # משחק משחק אקראי עד סופו
        # עבור כל הלוחות שהיו במהלך המשחק, הוא נותן להם ניקוד דרך הפונקציה board_score
        self.board = Board()
        self.board.set_to_start()
        win = False
        black_score = 0
        white_score = 0
        boards = []
        count =0
        while not win:
            b = self.do_random_move(self.board)
            count+=1
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
        left = len(boards)
        for board_str in boards:
            self.board_score(board_str)
            left-=1
            print(i, left, board_str, self.board_scores.get(board_str))
        data = json.dumps(self.board_scores)
        file = open('avalonscores.json', 'w')
        file.write(data)
        file.close()
        return count

    def do_random_move(self,board):
        # משחק מהלך אקראי אחד
        moves = board.all_ligel_moves()
        move_index = random.randrange(0,len(moves))
        selected_move = moves[move_index]
        b, i,j = board.make_a_move(selected_move[0][0],selected_move[0][1],selected_move[1])
        board.change_turn()
        return b
    def random_until_fall(self,board,moves):
        # משחק מהלכים אקראיים החל מהלוח הנתון עד שכדור אחד נופל
        # מחזיר איזה כדור נפל וכמה מהלכים הוא שיחק
        # מספר המהלכים מגבל לפרמטר moves
        count = 0
        while count<moves:
            b = self.do_random_move(board)
            count += 1
            if b:
                return count, State.OTHER[board.turn]
        return count, None

    def board_score(self, board_str):
        # בהנתן לוח, הפונקציה מחשבת את הניקוד שלו לפי ניקוד המשחק הנוכחי
        # ולפי מספר הצעדים המנימנים לנפילת כדור שחור/לבן שמחזירה פונקציה until_a_ball_fall
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

        b, w = self.until_a_ball_fall(board_str)
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