class Board:

    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]
        self.del_fig = []

# class Move:
    
#     def move(self, x, y):
#         pass

# class DiagonalMove(Move):

#     def move(self, x, y):
#         self.x = x

class ChessPiece:

    def __init__(self, x, y, color):
        self.position = [x, y]
        self.color = color

    def move(self, x, y):
        pass

class Pawn(ChessPiece):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.first_move = True

    def move(self, x, y):   # self.x - исходная координата
        if self.color == "b":
            if self.first_move:
                if ((x - self.x) == 1 or (x - self.x) == 2) and y == self.y:
                    if (not Board.board[x][y]) and (not Board.board[self.x+1][y]):
                        self.x = x
                        self.y = y
            else:
                if (x - self.x) == 1 and y == self.y:
                    if not Board.board[x][y]:
                        self.x = x
                        self.y = y
        if self.color == "w":
            if self.first_move:
                if ((self.x - x) == 1 or (self.x - x) == 2) and y == self.y:
                    if (not Board.board[x][y]) and (not Board.board[self.x-1][y]):
                        self.x = x
                        self.y = y
            else:
                if (x - self.x) == -1 and y == self.y:
                    if not Board.board[x][y]:
                        self.x = x
                        self.y = y

            

