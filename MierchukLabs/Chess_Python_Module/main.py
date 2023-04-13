import random


class ChessBoard:
    def __init__(self):
        self.board = [[None for i in range(8)] for j in range(8)]

    def print_board(self):
        for i in range(8):
            for j in range(8):
                print(self.board[i][j], end=' ')
            print()


class ChessPiece:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_possible_moves(self):
        pass


class King(ChessPiece):
    def __init__(self, name, position):
        super().__init__(name, position)

    def get_possible_moves(self):
        moves = []
        x, y = self.position
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                new_x, new_y = x + i, y + j
                if new_x >= 0 and new_x < 8 and new_y >= 0 and new_y < 8:
                    moves.append((new_x, new_y))
        return moves


class Bishop(ChessPiece):
    def __init__(self, name, position):
        super().__init__(name, position)

    def get_possible_moves(self):
        moves = []
        x, y = self.position
        for i in range(-7, 8):
            if i == 0:
                continue
            new_x, new_y = x + i, y + i
            if new_x >= 0 and new_x < 8 and new_y >= 0 and new_y < 8:
                moves.append((new_x, new_y))
            new_x, new_y = x + i, y - i
            if new_x >= 0 and new_x < 8 and new_y >= 0 and new_y < 8:
                moves.append((new_x, new_y))
        return moves


class ChessGame:
    def __init__(self):
        self.board = ChessBoard()
        self.pieces = []
        self.create_random_pieces()

    def create_random_pieces(self):
        piece_names = ['K1', 'K2', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6']
        for name in piece_names:
            piece_type = random.choice(['king', 'bishop'])
            x, y = random.randint(0, 7), random.randint(0, 7)
            if piece_type == 'king':
                piece = King(name, (x, y))
            else:
                piece = Bishop(name, (x, y))
            self.pieces.append(piece)
            self.board.board[x][y] = name

    def start(self):
        self.board.print_board()
        while True:
            piece_name = input('Enter the name of the piece you want to move: ')
            piece = None
            for p in self.pieces:
                if p.name == piece_name:
                    piece = p
                    break
            if not piece:
                print('Invalid piece name. Please try again.')
                continue
            moves = piece.get_possible_moves()
            print(f'Possible moves for {piece_name}: {moves}')
            break


game = ChessGame()
game.start()
