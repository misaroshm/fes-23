#in this file: both Board and Game classes

from typing import List, Tuple, Union
from pieces import Piece, CELL, Pawn, Rook, Bishop, Knight, Queen, King

class PieceFactory:
    """
        Desc: PieceFactory class have only one method and is used to create a
              certain type of Piece with a given coordinates. it is factory pattern thing.
    """
    @staticmethod
    def set_piece(board, piece_type: str, color: Union[str, None], row: int, col: int) -> Piece:
        if piece_type == "CELL":
            return CELL(row, col, board)
        elif color not in ("white", "black"):
            raise ValueError("Invalid colour")
        # chess army
        if piece_type == "Pawn":
            return Pawn(color, row, col, board)
        elif piece_type == "Rook":
            return Rook(color, row, col, board)
        elif piece_type == "Bishop":
            return Bishop(color, row, col, board)
        elif piece_type == "Knight":
            return Knight(color, row, col, board)
        elif piece_type == "Queen":
            return Queen(color, row, col, board)
        elif piece_type == "King":
            return King(color, row, col, board)
        else:
            raise ValueError("Invalid piece type")

class Board:
    """
        Desc: This class represents a chess board.
    """
    def __init__(self) -> None:
        self.piece_handler = PieceFactory()              # piece creator field
        self.board = [[self.piece_handler.set_piece(self, "CELL", None, 0, 0)] * 8 for y in range(8)]
        self.create_board()                             # just init board
        self.start_pawn_moved = False                   # for first Pawn move when game is started.

    def create_board(self) -> None:
        # init pieces on the board
        # blacks
        self.board[0][0] = self.piece_handler.set_piece(self, "Rook", "black", 0, 0)
        self.board[0][1] = self.piece_handler.set_piece(self, "Knight", "black", 0, 1)
        self.board[0][2] = self.piece_handler.set_piece(self, "Bishop", "black", 0, 2)
        self.board[0][3] = self.piece_handler.set_piece(self, "Queen", "black", 0, 3)
        self.board[0][4] = self.piece_handler.set_piece(self, "King", "black", 0, 4)
        self.board[0][5] = self.piece_handler.set_piece(self, "Bishop", "black", 0, 5)
        self.board[0][6] = self.piece_handler.set_piece(self, "Knight", "black", 0, 6)
        self.board[0][7] = self.piece_handler.set_piece(self, "Rook", "black", 0, 7)
        for i in range(8):
            self.board[1][i] = self.piece_handler.set_piece(self, "Pawn", "black", 1, i)
        # whites
        self.board[7][0] = self.piece_handler.set_piece(self, "Rook", "white", 7, 0)
        self.board[7][1] = self.piece_handler.set_piece(self, "Knight", "white", 7, 1)
        self.board[7][2] = self.piece_handler.set_piece(self, "Bishop", "white", 7, 2)
        self.board[7][3] = self.piece_handler.set_piece(self, "Queen", "white", 7, 3)
        self.board[7][4] = self.piece_handler.set_piece(self, "King", "white", 7, 4)
        self.board[7][5] = self.piece_handler.set_piece(self, "Bishop", "white", 7, 5)
        self.board[7][6] = self.piece_handler.set_piece(self, "Knight", "white", 7, 6)
        self.board[7][7] = self.piece_handler.set_piece(self, "Rook", "white", 7, 7)
        for i in range(8):
            self.board[6][i] = self.piece_handler.set_piece(self, "Pawn", "white", 6, i)
        # init default cells on the board
        for i in range(2, 6):
            for j in range(8):
                self.board[i][j] = self.piece_handler.set_piece(self, "CELL", None, i, j)

    def move_piece_if_to_is_valid(self, row: int, col: int, to_row: int, to_col: int) -> bool:
        if not self.is_valid_coords(row, col) or not self.is_valid_coords(to_row, to_col):
            print("Coordinates is not valid!")
            return False
        piece = self.board[row][col]
        if piece.type == 'NULL':
            print(f"No piece is found in this position: {row}{col}")
            return False
        if not piece.can_move(row, col, to_row, to_col):
            print(f"Move to {to_row}, {to_col} is Invalid for {piece.type}")
            return False
        else:
            print(f"Successful move.")
            self.board[to_row][to_col] = piece
            self.board[row][col] = self.piece_handler.set_piece(self, "CELL", None, row, col)
            return True

    def is_valid_coords(self, row: int, col: int) -> bool:
        return 0 <= row < 8 and 0 <= col < 8

    def is_empty(self, row: int, col: int) -> bool:
        return self.board[row][col].type == "NULL"

    def get_piece(self, row: int, col: int) -> Piece | None:    # -> Union(Piece, None): -  doesnt work i dont know, buut -> Piece | None: is the same
        if not self.is_valid_coords(row, col):
            return None
        piece = self.board[row][col]
        if piece == CELL:
            return None
        else: return piece

    def __str__(self) -> str:
        print("⌜|a||b||c||d||e||f||g||h|⌝")
        res = ''
        for y in range(8):
            res += str(8 - y) + ' |' + '|'.join(map(str, self.board[y])) + f"| {str(8 - y)}\n"
        return res + "⌞|a||b||c||d||e||f||g||h|⌟"


# not now, all in board now
class Game:
    pass
