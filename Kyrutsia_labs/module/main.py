
from abc import ABC, abstractmethod


class Piece(ABC):
    @abstractmethod
    def __str__(self):
        pass


class King(Piece):
    def __str__(self):
        return "K"


class Queen(Piece):
    def __str__(self):
        return "Q"


class Bishop(Piece):
    def __str__(self):
        return "B"


class Knight(Piece):
    def __str__(self):
        return "N"


class Rook(Piece):
    def __str__(self):
        return "R"


class Pawn(Piece):
    def __str__(self):
        return "P"


class PieceFactory(ABC):
    @abstractmethod
    def create_piece(self):
        pass


class WhitePieceFactory(PieceFactory):
    def create_piece(self, piece_type):
        if piece_type == "K":
            return King()
        elif piece_type == "Q":
            return Queen()
        elif piece_type == "B":
            return Bishop()
        elif piece_type == "N":
            return Knight()
        elif piece_type == "R":
            return Rook()
        elif piece_type == "P":
            return Pawn()


class BlackPieceFactory(PieceFactory):
    def create_piece(self, piece_type):
        if piece_type == "K":
            return King()
        elif piece_type == "Q":
            return Queen()
        elif piece_type == "B":
            return Bishop()
        elif piece_type == "N":
            return Knight()
        elif piece_type == "R":
            return Rook()
        elif piece_type == "P":
            return Pawn()


class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def place_piece(self, piece, row, col):
        self.board[row][col] = piece

    def __str__(self):
        result = ""
        for row in range(8):
            for col in range(8):
                if self.board[row][col] is not None:
                    result += str(self.board[row][col])
                else:
                    result += "."
            result += "\n"
        return result


class Game:
    def __init__(self):
        self.board = Board()
        self.white_piece_factory = WhitePieceFactory()
        self.black_piece_factory = BlackPieceFactory()

    def setup(self):
        # Place white pieces
        for col, piece_type in enumerate("RNBQKBNR"):
            self.board.place_piece(self.white_piece_factory.create_piece(piece_type), 0, col)
        for col in range(8):
            self.board.place_piece(self.white_piece_factory.create_piece("P"), 1, col)

        # Place black pieces
        for col, piece_type in enumerate("RNBQKBNR"):
            self.board.place_piece(self.black_piece_factory.create_piece(piece_type), 7, col)
        for col in range(8):
            self.board.place_piece(self.black_piece_factory.create_piece("P"), 6, col)

    def play(self):
        print(self.board)


game = Game()
game.setup()
game.play()