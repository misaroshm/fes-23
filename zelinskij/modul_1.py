class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]

    def draw(self):
        for i in range(8):
            print('+---' * 8 + '+')
            for j in range(8):
                print('| {} '.format(self.board[i][j]), end='')
            print('|')
        print('+---' * 8 + '+')

class Piece:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col

class Pawn(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.piece_type = 'pawn'

class Rook(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.piece_type = 'rook'

class Knight(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.piece_type = 'knight'

class Bishop(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.piece_type = 'bishop'

class Queen(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.piece_type = 'queen'

class King(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.piece_type = 'king'

class PieceFactory:
    def create_piece(self, piece_type, color, row, col):
        if piece_type == 'pawn':
            return Pawn(color, row, col)
        elif piece_type == 'rook':
            return Rook(color, row, col)
        elif piece_type == 'knight':
            return Knight(color, row, col)
        elif piece_type == 'bishop':
            return Bishop(color, row, col)
        elif piece_type == 'queen':
            return Queen(color, row, col)
        elif piece_type == 'king':
            return King(color, row, col)

class Game:
    def __init__(self):
        self.board = Board()
        self.pieces = []
        self.piece_factory = PieceFactory()
        self.setup_board()

    def setup_board(self):
        # розміщуємо фігури на дошці
        self.pieces.append(self.piece_factory.create_piece('rook', 'white', 0, 0))
        self.pieces.append(self.piece_factory.create_piece('knight', 'white', 0, 1))
        self.pieces.append(self.piece_factory.create_piece('bishop', 'white', 0, 2))
        self.pieces.append(self.piece_factory.create_piece('queen', 'white', 0, 3))
        self.pieces.append(self.piece_factory.create_piece('king', 'white', 0, 4))
        self.pieces.append(self.piece_factory.create_piece('bishop', 'white', 0, 5))
        self.pieces.append(self.piece_factory.create_piece('knight', 'white', 0, 6))
        self.pieces.append(self.piece_factory.create_piece('rook', 'white', 0, 7))
        for i in range(8):
            self.pieces.append(self.piece_factory.create_piece('pawn', 'white', 1, i))
            self.pieces.append(self.piece_factory.create_piece('pawn', 'black', 6, i))
        self.pieces.append(self.piece_factory.create_piece('rook', 'black', 7, 0))
        self.pieces.append(self.piece_factory.create_piece('knight', 'black', 7, 1))
        self.pieces.append(self.piece_factory.create_piece('bishop', 'black', 7, 2))
        self.pieces.append(self.piece_factory.create_piece('queen', 'black', 7, 3))
        self.pieces.append(self.piece_factory.create_piece('king', 'black', 7, 4))
        self.pieces.append(self.piece_factory.create_piece('bishop', 'black', 7, 5))
        self.pieces.append(self.piece_factory.create_piece('knight', 'black', 7, 6))
        self.pieces.append(self.piece_factory.create_piece('rook', 'black', 7, 7))


        # оновлюємо дошку
        for piece in self.pieces:
            self.board.board[piece.row][piece.col] = piece.piece_type[0]

    def draw(self):
        self.board.draw()

game = Game()
game.draw()