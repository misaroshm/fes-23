from abc import ABC, abstractmethod

class Piece(ABC):
    @abstractmethod
    def move(self):
        pass

class Pawn(Piece):
    def move(self):
        print("Pawn moved")

class Rook(Piece):
    def move(self):
        print("Rook moved")

class Knight(Piece):
    def move(self):
        print("Knight moved")

class Bishop(Piece):
    def move(self):
        print("Bishop moved")

class Queen(Piece):
    def move(self):
        print("Queen moved")

class King(Piece):
    def move(self):
        print("King moved")

class PieceFactory:
    @staticmethod
    def create_piece(piece_type):
        if piece_type == "pawn":
            return Pawn()
        elif piece_type == "rook":
            return Rook()
        elif piece_type == "knight":
            return Knight()
        elif piece_type == "bishop":
            return Bishop()
        elif piece_type == "queen":
            return Queen()
        elif piece_type == "king":
            return King()
        else:
            raise ValueError("Invalid piece type")

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self._populate_board()

    def _populate_board(self):
        for i in range(8):
            self.board[1][i] = PieceFactory.create_piece("pawn")
            self.board[6][i] = PieceFactory.create_piece("pawn")

        self.board[0][0] = PieceFactory.create_piece("rook")
        self.board[0][1] = PieceFactory.create_piece("knight")
        self.board[0][2] = PieceFactory.create_piece("bishop")
        self.board[0][3] = PieceFactory.create_piece("queen")
        self.board[0][4] = PieceFactory.create_piece("king")
        self.board[0][5] = PieceFactory.create_piece("bishop")
        self.board[0][6] = PieceFactory.create_piece("knight")
        self.board[0][7] = PieceFactory.create_piece("rook")

        self.board[7][0] = PieceFactory.create_piece("rook")
        self.board[7][1] = PieceFactory.create_piece("knight")
        self.board[7][2] = PieceFactory.create_piece("bishop")
        self.board[7][3] = PieceFactory.create_piece("queen")
        self.board[7][4] = PieceFactory.create_piece("king")
        self.board[7][5] = PieceFactory.create_piece("bishop")
        self.board[7][6] = PieceFactory.create_piece("knight")
        self.board[7][7] = PieceFactory.create_piece("rook")

class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = "white"

    def play(self):
        while True:
            self._display_board()
            move = input(f"{self.current_player}'s move: ")
            # process move logic

            self.current_player = "black" if self.current_player == "white" else "white"

    def _display_board(self):
        for row in self.board.board:
            for piece in row:
                if piece:
                    print(type(piece).__name__[0], end=" ")
                else:
                    print("-", end=" ")
            print()

game = Game()
game.play()