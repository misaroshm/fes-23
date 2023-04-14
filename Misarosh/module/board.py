import copy


class Board:
    def __init__(self):
        # Filling chessboard with pieces
        self.board = [[(0, 0) for i in range(8)] for j in range(8)]

        # Tuple of (type_of_piece, color)
        self.board[0][0] = (1, 'B')
        self.board[0][1] = (2, 'B')
        self.board[0][6] = (2, 'B')
        self.board[0][7] = (1, 'B')

        self.board[1][0] = (6, 'B')
        self.board[1][2] = (6, 'B')
        self.board[1][4] = (6, 'B')
        self.board[1][7] = (6, 'B')

        self.board[7][0] = (1, 'W')
        self.board[7][3] = (4, 'W')
        self.board[7][4] = (5, 'W')
        self.board[7][5] = (3, 'W')

        self.board[6][3] = (6, 'W')
        self.board[6][4] = (6, 'W')
        self.board[6][5] = (6, 'W')

        # Available moves for knight matrix
        self.knight_move_matrix = [[0, 1, 0, 1, 0],
                                   [1, 0, 0, 0, 1],
                                   [0, 0, 0, 0, 0],
                                   [1, 0, 0, 0, 1],
                                   [0, 1, 0, 1, 0]]

        self.previous_board = copy.deepcopy(self.board)

        self.undo_flag = False

        self.white_king_pos = (4, 7)
        self.black_king_pos = (4, 0)

    # Drawing the chessboard in terminal
    def draw_chessboard(self):
        print("  A   B   C   D   E   F   G   H")
        print('---------------------------------')
        for i in range(8):
            for j in range(8):
                print('|', end=' ')
                if self.board[i][j][0] == 0:
                    print(' ', end=' ')
                elif self.board[i][j][0] == 1:
                    print('R', end=' ')
                elif self.board[i][j][0] == 2:
                    print('N', end=' ')
                elif self.board[i][j][0] == 3:
                    print('B', end=' ')
                elif self.board[i][j][0] == 4:
                    print('Q', end=' ')
                elif self.board[i][j][0] == 5:
                    print('K', end=' ')
                elif self.board[i][j][0] == 6:
                    print('P', end=' ')
            print('|', end=' ')
            print(8 - i)
            print('---------------------------------')