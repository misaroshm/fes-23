#Інструкція по використанню коду в консолі:

#Запустіть код у середовищі Python.
#Відобразиться початкова шахова дошка з пустими клітинками.
#При введенні команди "Enter the starting position of the piece:", введіть позицію фігури, яку ви хочете перемістити. Наприклад, "a2" або "b1".
#При введенні команди "Enter the end position of the piece:", введіть позицію, куди ви хочете перемістити фігуру.
#Код перевірить чи може фігура переміститися до вказаної позиції і виконає переміщення, якщо це можливо. В іншому випадку, буде виведено повідомлення про недійсний хід.
#Гра продовжиться з наступним гравцем.
#from typing import Tuple
#
class Piece:
    def __init__(self, board, name, color, row, col):
        self.board = board
        self.name = name
        self.color = color
        self.row = row
        self.col = col

    def can_move(self, row, col):
        raise NotImplementedError()

    def get_representation(self):
        if self.color == "white":
            return self.name[0].upper()
        else:
            return self.name[0].lower()

class Pawn(Piece):
    def can_move(self, row, col):
        if self.color == "white":
            if row == self.row - 1 and col == self.col:
                return True
        else:
            if row == self.row + 1 and col == self.col:
                return True
        return False

class Rook(Piece):
    def can_move(self, row, col):
        if row == self.row or col == self.col:
            return True
        return False

class Knight(Piece):
    def can_move(self, row, col):
        if abs(row - self.row) == 2 and abs(col - self.col) == 1:
            return True
        if abs(row - self.row) == 1 and abs(col - self.col) == 2:
            return True
        return False

class Bishop(Piece):
    def can_move(self, row, col):
        if abs(row - self.row) == abs(col - self.col):
            return True
        return False

class Queen(Piece):
    def can_move(self, row, col):
        if row == self.row or col == self.col:
            return True
        if abs(row - self.row) == abs(col - self.col):
            return True
        return False

class King(Piece):
    def can_move(self, row, col):
        if abs(row - self.row) <= 1 and abs(col - self.col) <= 1:
            return True
        return False

class Board:
    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]
        self.piece_factory = PieceFactory()

        # Create pieces for black side
        self.board[0][0] = self.piece_factory.create_piece(self, "Rook", "black", 0, 0)
        self.board[0][1] = self.piece_factory.create_piece(self, "Knight", "black", 0, 1)
        self.board[0][2] = self.piece_factory.create_piece(self, "Bishop", "black", 0, 2)
        self.board[0][3] = self.piece_factory.create_piece(self, "Queen", "black", 0, 3)
        self.board[0][4] = self.piece_factory.create_piece(self, "King", "black", 0, 4)
        self.board[0][5] = self.piece_factory.create_piece(self, "Bishop", "black", 0, 5)
        self.board[0][6] = self.piece_factory.create_piece(self, "Knight", "black", 0, 6)
        self.board[0][7] = self.piece_factory.create_piece(self, "Rook", "black", 0, 7)
        for col in range(8):
            self.board[1][col] = self.piece_factory.create_piece(self, "Pawn", "black", 1, col)

        # Create pieces for white side
        self.board[7][0] = self.piece_factory.create_piece(self, "Rook", "white", 7, 0)
        self.board[7][1] = self.piece_factory.create_piece(self, "Knight", "white", 7, 1)
        self.board[7][2] = self.piece_factory.create_piece(self, "Bishop", "white", 7, 2)
        self.board[7][3] = self.piece_factory.create_piece(self, "Queen", "white", 7, 3)
        self.board[7][4] = self.piece_factory.create_piece(self, "King", "white", 7, 4)
        self.board[7][5] = self.piece_factory.create_piece(self, "Bishop", "white", 7, 5)
        self.board[7][6] = self.piece_factory.create_piece(self, "Knight", "white", 7, 6)
        self.board[7][7] = self.piece_factory.create_piece(self, "Rook", "white", 7, 7)
        for col in range(8):
            self.board[6][col] = self.piece_factory.create_piece(self, "Pawn", "white", 6, col)

    def is_valid_position(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def get_piece(self, row, col):
        if self.is_valid_position(row, col):
            return self.board[row][col]
        return None

class PieceFactory:
    def create_piece(self, board, name, color, row, col):
        if name == "Pawn":
            return Pawn(board, name, color, row, col)
        if name == "Rook":
            return Rook(board, name, color, row, col)
        if name == "Knight":
            return Knight(board, name, color, row, col)
        if name == "Bishop":
            return Bishop(board, name, color, row, col)
        if name == "Queen":
            return Queen(board, name, color, row, col)
        if name == "King":
            return King(board, name, color, row, col)
        raise ValueError("Invalid piece name")

def parse_position(position: str) -> Tuple[int, int]:
    col = ord(position[0].lower()) - ord('a')
    row = int(position[1]) - 1
    return row, col

def play_chess():
    board = Board()
    while True:
        print_board(board)
        start_position = input("Enter the starting position of the piece: ")
        end_position = input("Enter the end position of the piece: ")

        start_row, start_col = parse_position(start_position)
        end_row, end_col = parse_position(end_position)

        piece = board.get_piece(start_row, start_col)

        if piece is None:
            print("There is no piece at the specified position.")
            continue

        if not piece.can_move(end_row, end_col):
            print("The piece cannot move to the specified position.")
            continue

        board.board[start_row][start_col] = None
        board.board[end_row][end_col] = piece

def print_board(board):
    for row in range(8):
        for col in range(8):
            piece = board.get_piece(row, col)
            if piece is None:
                print(".", end=" ")
            else:
                print(piece.get_representation(), end=" ")
        print()

play_chess()
