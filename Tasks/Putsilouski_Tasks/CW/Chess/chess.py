class Board:
    def __init__(self):
        self.del_fig_w = []
        self.del_fig_b = []
        self.board = []
        # Послание всем, кто это увидит:
        # Дорогой друг, запомни: X это не X, - это Y
        #                        Y это не Y, - это X
        # Всё не то, чем кажется на самом деле...
        for x, i in enumerate('87654321'):
            self.board.append([])
            for y, j in enumerate('ABCDEFGH'):
                if i in '81':
                    if j in 'AH':
                        self.board[-1].append(Rook())
                    elif j in 'BG':
                        self.board[-1].append(Knight(x, y, 'wb'[i == '7']))
                    elif j in 'CF':
                        self.board[-1].append(Bishop())
                    elif j == 'D':
                        self.board[-1].append(Queen())
                    elif j == 'E':
                        self.board[-1].append(King(x, y, 'wb'[i == '7']))
                    self.board[-1][-1].x = x
                    self.board[-1][-1].y = y
                    self.board[-1][-1].color = 'wb'[i == '8']
                elif i in '72':
                    self.board[-1].append(Pawn(x=x, y=y, color='wb'[i == '7']))
                else:
                    self.board[-1].append(0)


class ChessPiece:

    def __init__(self, x=None, y=None, color=None):
        self.x = x
        self.y = y
        self.color = color
        self.fig_type = ''

    def __str__(self):
        return f'{"White" if self.color == "w" else "Black"} {self.__class__.__name__.lower()} at {self.x, self.y}'

    def __repr__(self):
        return f'{"White" if self.color == "w" else "Black"} {self.__class__.__name__.lower()} at {self.x, self.y}'

    def legal_moves(self, board):
        pass


class Rook(ChessPiece):
    def __init__(self, x=None, y=None, color=None):
        super().__init__(x, y, color)
        self.fig_type = 'Л'


class Knight(ChessPiece):

    def __init__(self, x=None, y=None, color=None):
        super().__init__(x, y, color)
        self.fig_type = 'К'

    def legal_moves(self, board):
        self.board = board
        legal_moves_list = []
        i = (1, -1)[self.color == 'w']

        if 0 <= self.x + i <= 7:
            if (0 <= self.y + 2 <= 7) and self.board[self.x + i][self.y + 2] and (
                    self.board[self.x + i][self.y + 2].color != self.board[self.x][self.y].color):
                legal_moves_list.append(to_fide([self.x + i, self.y + 2]))
            if (0 <= self.y - 2 <= 7) and self.board[self.x + i][self.y - 2] and (
                    self.board[self.x + i][self.y - 2].color != self.board[self.x][self.y].color):
                legal_moves_list.append(to_fide([self.x + i, self.y - 2]))
            if 0 <= self.y - 2 <= 7:
                if not self.board[self.x + i][self.y - 2]:
                    legal_moves_list.append(to_fide([self.x + i, self.y - 2]))
            if 0 <= self.y + 2 <= 7:
                if not self.board[self.x + i][self.y + 2]:
                    legal_moves_list.append(to_fide([self.x + i, self.y + 2]))

        if 0 <= self.x - i <= 7:
            if (0 <= self.y + 2 <= 7) and self.board[self.x - i][self.y + 2] and (
                    self.board[self.x - i][self.y + 2].color != self.board[self.x][self.y].color):
                legal_moves_list.append(to_fide([self.x - i, self.y + 2]))
            if (0 <= self.y - 2 <= 7) and self.board[self.x - i][self.y - 2] and (
                    self.board[self.x - i][self.y - 2].color != self.board[self.x][self.y].color):
                legal_moves_list.append(to_fide([self.x - i, self.y - 2]))
            if 0 <= self.y + 2 <= 7:
                if not self.board[self.x - i][self.y + 2]:
                    legal_moves_list.append(to_fide([self.x - i, self.y + 2]))
            if 0 <= self.y - 2 <= 7:
                if not self.board[self.x - i][self.y - 2]:
                    legal_moves_list.append(to_fide([self.x - i, self.y - 2]))

        if 0 <= self.x + i * 2 <= 7:
            if (0 <= self.y + 1 <= 7) and self.board[self.x + i * 2][self.y + 1] and (
                    self.board[self.x + i * 2][self.y + 1].color != self.board[self.x][self.y].color):
                legal_moves_list.append(to_fide([self.x + i * 2, self.y + 1]))
            if (0 <= self.y - 1 <= 7) and self.board[self.x + i * 2][self.y - 1] and (
                    self.board[self.x + i * 2][self.y - 1].color != self.board[self.x][self.y].color):
                legal_moves_list.append(to_fide([self.x + i * 2, self.y - 1]))
            if 0 <= self.y + 1 <= 7:
                if not self.board[self.x + i * 2][self.y + 1]:
                    legal_moves_list.append(to_fide([self.x + i * 2, self.y + 1]))
            if 0 <= self.y - 1 <= 7:
                if not self.board[self.x + i * 2][self.y - 1]:
                    legal_moves_list.append(to_fide([self.x + i * 2, self.y - 1]))

        if 0 <= self.x - i * 2 <= 7:
            if (0 <= self.y + 1 <= 7) and self.board[self.x - i * 2][self.y + 1] and (
                    self.board[self.x - i * 2][self.y + 1].color != self.board[self.x][self.y].color):
                legal_moves_list.append(to_fide([self.x - i * 2, self.y + 1]))
            if (0 <= self.y - 1 <= 7) and self.board[self.x - i * 2][self.y - 1] and (
                    self.board[self.x - i * 2][self.y - 1].color != self.board[self.x][self.y].color):
                legal_moves_list.append(to_fide([self.x - i * 2, self.y - 1]))
            if 0 <= self.y + 1 <= 7:
                if not self.board[self.x - i * 2][self.y + 1]:
                    legal_moves_list.append(to_fide([self.x - i * 2, self.y + 1]))
            if 0 <= self.y - 1 <= 7:
                if not self.board[self.x - i * 2][self.y - 1]:
                    legal_moves_list.append(to_fide([self.x - i * 2, self.y - 1]))

        return legal_moves_list


class Bishop(ChessPiece):
    def __init__(self, x=None, y=None, color=None):
        super().__init__(x, y, color)
        self.fig_type = 'С'


class Queen(ChessPiece):
    def __init__(self, x=None, y=None, color=None):
        super().__init__(x, y, color)
        self.fig_type = 'Ф'


class King(ChessPiece):
    def __init__(self, x=None, y=None, color=None):
        super().__init__(x, y, color)
        self.fig_type = 'Кр'

    def legal_moves(self, board):
        self.board = board
        legal_moves_list = []
        self.moves_temp = []
        for i in range(8):
            for k in range(8):
                if self.board[i][k] and self.board[i][k].color != self.color and self.board[i][k].fig_type != 'Кр' and \
                        self.board[i][k].fig_type:
                    if self.board[i][k].legal_moves(self.board):
                        self.moves_temp = self.moves_temp + self.board[i][k].legal_moves(self.board)
                elif self.board[i][k] and self.board[i][k].color != self.color and not self.board[i][k].fig_type:
                    self.board[i][k].legal_moves(self.board)
                    self.moves_temp = self.moves_temp + self.board[i][k].attack_moves
        self.moves_temp = list(set(self.moves_temp))

        if 0 <= self.x + 1 <= 7:
            if self.board[self.x + 1][self.y] and (
                    self.board[self.x + 1][self.y].color != self.board[self.x][self.y].color):
                legal_moves_list.append(to_fide([self.x + 1, self.y]))
            if (0 <= self.y + 1 <= 7) and self.board[self.x + 1][self.y + 1] and (
                    self.board[self.x + 1][self.y + 1].color != self.board[self.x][self.y].color):
                legal_moves_list.append(to_fide([self.x + 1, self.y + 1]))
            if (0 <= self.y <= 7) and self.board[self.x + 1][self.y - 1] and (
                    self.board[self.x + 1][self.y - 1].color != self.board[self.x][self.y].color):
                legal_moves_list.append(to_fide([self.x + 1, self.y - 1]))
            if 0 <= self.y + 1 <= 7:
                if not self.board[self.x + 1][self.y + 1] and (
                        to_fide([self.x + 1, self.y + 1]) not in self.moves_temp):
                    legal_moves_list.append(to_fide([self.x + 1, self.y + 1]))
            if 0 <= self.y - 1 <= 7:
                if not self.board[self.x + 1][self.y - 1] and (
                        to_fide([self.x + 1, self.y - 1]) not in self.moves_temp):
                    legal_moves_list.append(to_fide([self.x + 1, self.y - 1]))
            if not self.board[self.x + 1][self.y] and (to_fide([self.x + 1, self.y]) not in self.moves_temp):
                legal_moves_list.append(to_fide([self.x + 1, self.y]))

        if 0 <= self.y - 1 <= 7:
            if self.board[self.x - 1][self.y] and (
                    self.board[self.x - 1][self.y].color != self.board[self.x][self.y].color):
                legal_moves_list.append(to_fide([self.x - 1, self.y]))
            if (0 <= self.y - 1 <= 7) and self.board[self.x - 1][self.y + 1] and (
                    self.board[self.x - 1][self.y + 1].color != self.board[self.x][self.y].color):
                legal_moves_list.append(to_fide([self.x - 1, self.y + 1]))
            if (0 <= self.y - 1 <= 7) and self.board[self.x - 1][self.y - 1] and (
                    self.board[self.x - 1][self.y - 1].color != self.board[self.x][self.y].color):
                legal_moves_list.append(to_fide([self.x - 1, self.y - 1]))
            if 0 <= self.y - 1 <= 7:
                if not self.board[self.x - 1][self.y + 1] and (
                        to_fide([self.x - 1, self.y + 1]) not in self.moves_temp):
                    legal_moves_list.append(to_fide([self.x - 1, self.y + 1]))
            if 0 <= self.y - 1 <= 7:
                if not self.board[self.x - 1][self.y - 1] and (
                        to_fide([self.x - 1, self.y - 1]) not in self.moves_temp):
                    legal_moves_list.append(to_fide([self.x - 1, self.y - 1]))
            if not self.board[self.x - 1][self.y] and (to_fide([self.x - 1, self.y]) not in self.moves_temp):
                legal_moves_list.append(to_fide([self.x - 1, self.y]))

        if 0 <= self.y - 1 <= 7:
            if self.board[self.x][self.y + 1] and (
                    self.board[self.x][self.y + 1].color != self.board[self.x][self.y].color):
                legal_moves_list.append(to_fide([self.x, self.y + 1]))
            if not self.board[self.x][self.y + 1] and (to_fide([self.x, self.y + 1]) not in self.moves_temp):
                legal_moves_list.append(to_fide([self.x, self.y + 1]))
        if 0 <= self.y - 1 <= 7:
            if self.board[self.x][self.y - 1] and (
                    self.board[self.x][self.y - 1].color != self.board[self.x][self.y].color):
                legal_moves_list.append(to_fide([self.x, self.y - 1]))
            if not self.board[self.x][self.y - 1] and (to_fide([self.x, self.y - 1]) not in self.moves_temp):
                legal_moves_list.append(to_fide([self.x, self.y - 1]))

        return legal_moves_list


class Pawn(ChessPiece):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.first_move = True
        self.fig_type = ''

    def legal_moves(self, board):
        self.board = board
        legal_moves_list = []
        self.attack_moves = []
        i = (1, -1)[self.color == 'w']
        if 0 <= self.x + i <= 7:
            if (0 <= self.y + 1 <= 7) and self.board[self.x + i][self.y + 1] and (
                    self.board[self.x + i][self.y + 1].color != self.board[self.x][self.y].color):
                legal_moves_list.append(to_fide([self.x + i, self.y + 1]))
            if (0 <= self.y - 1 <= 7) and self.board[self.x + i][self.y - 1] and (
                    self.board[self.x + i][self.y - 1].color != self.board[self.x][self.y].color):
                legal_moves_list.append(to_fide([self.x + i, self.y - 1]))
            if not self.board[self.x + i][self.y]:
                legal_moves_list.append(to_fide([self.x + i, self.y]))
        if self.first_move:
            if not self.board[self.x + i * 2][self.y]:
                legal_moves_list.append(to_fide([self.x + i * 2, self.y]))
        if 0 <= self.x + i <= 7:
            if 0 <= self.y - 1 <= 7:
                self.attack_moves += [to_fide([self.x + i, self.y - 1])]
            if 0 <= self.y + 1 <= 7:
                self.attack_moves += [to_fide([self.x + i, self.y + 1])]
        return legal_moves_list


def to_fide(step):
    return 'abcdefgh'[step[1]] + '87654321'[step[0]]


def from_fide(step):
    return ['87654321'.index(step[1]), 'abcdefgh'.index(step[0])]


if __name__ == '__main__':
    b = Board()
    for i in b.board:
        print('-' * 10)
        for j in i:
            print(j)

    print(b.board[1][1].legal_moves(b.board))
    print(b.board[1][1].attack_moves)

    print(to_fide([4, 4]))
    b.board[4][4] = King(4, 4, 'w')
    print(b.board[4][4].legal_moves(b.board))
    print(b.board[4][4].moves_temp)
