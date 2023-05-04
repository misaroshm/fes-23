# In this file: the Piece itself, and some Piece<Type> classes

from abc import ABC, abstractmethod
from typing import List, Tuple, Union, TYPE_CHECKING
if TYPE_CHECKING:
    from board import Board

# Possible pieces types
TYPES = ('NULL', 'Pawn', 'Knight', 'Bishop', 'Rook', 'Queen', 'King')

# this is an abstract method of some kind of piece
class Piece(ABC):

    def __init__(self, color: Union[str, None], row: int, col: int, board: 'Board') -> None:
        self.board = board          # &board reference
        self.color = color          # "white" or "black"
        self.row = row              # the row or the X
        self.col = col              # the column or the Y
        self.symbol = '⬜'           # unicode symbol; default is for NULL
        self.dropped = False        # piece is on board or not
        self.type = TYPES[0]       # default is NULL

    """ Desc: represents whether move is valid or not """
    @abstractmethod
    def can_move(self, cur_row: int, cur_col: int, to_row: int, to_col: int) -> bool:
        pass

    """ Desc: both __str__ and __repr__ string representations for the class """
    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass


class CELL(Piece):
    """ Desc: this is not a figure but a part of field too! """
    def __init__(self, row: int, col: int, board: 'Board') -> None:
        super().__init__(None, row, col, board)

    def can_move(self, cur_row: int, cur_col: int, to_row: int, to_col: int) -> None:
        return False

    def __str__(self) -> str:
        return self.symbol

    def __repr__(self) -> str:
        return f"CELL('{self.row}, {self.col})"

class Pawn(Piece):
    def __init__(self, color: str, row: int, col: int, board: 'Board') -> None:
        super().__init__(color, row, col, board)
        self.type = TYPES[1]
        if self.color == "white":
            self.symbol = '♙'
        else:
            self.symbol = '♟'

    # pawn move logic is implemented for now
    # implemented also a two moving if is first_move
    def can_move(self, cur_row: int, cur_col: int, to_row: int, to_col: int) -> bool:
        if self.color == 'white':
            direction = -1
            start_row = 6
        else:
            direction = 1
            start_row = 1

        # сheck if moving in the correct direction.
        if start_row != cur_row:
            if to_row - cur_row != direction:
                return False
        else:
            if to_row - cur_row not in (direction, 2*direction):
                return False

        # сheck if the pawn is moving straight forward
        if to_col == cur_col and self.board.is_empty(to_row, to_col):
            # If pawn is moving straight forward and destination is empty, it is valid move
            if to_row == start_row - direction or self.row == start_row:
                return True
        # сheck if the pawn is capturing a piece
        elif abs(to_col - cur_col) == 1 and to_row - cur_row == direction:
            target_piece = self.board.get_piece(to_row, to_col)
            if target_piece is not None and not CELL and target_piece.color != self.color:
                return True
        return False

    def __str__(self) -> str:
        return self.symbol

    def __repr__(self) -> str:
        return f"Pawn('{self.color}', {self.row}, {self.col})"


class Knight(Piece):
    def __init__(self, color: str, row: int, col: int, board: 'Board') -> None:
        super().__init__(color, row, col, board)
        self.type = TYPES[2]
        if self.color == "white":
            self.symbol = '♘'
        else:
            self.symbol = '♞'

    def can_move(self, cur_row: int, cur_col: int, to_row: int, to_col: int) -> bool:
        row_absoffset = abs(to_row - cur_row)
        col_absoffset = abs(to_col - cur_col)
        # The knight can move in an L-shape, i.e. move two squares vertically and one square horizontally,
        # or two squares horizontally and one square vertically
        if (row_absoffset, col_absoffset) == (1, 2) or (row_absoffset, col_absoffset) == (2, 1):
            # Check if the destination square is empty or has a piece of the opposite color
            target_piece = self.board.get_piece(to_row, to_col)
            if target_piece is None or target_piece.color != self.color:
                return True

        return False

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return f"Knight('{self.color}', {self.row}, {self.col})"


class Bishop(Piece):
    def __init__(self, color: str, row: int, col: int, board: 'Board') -> None:
        super().__init__(color, row, col, board)
        self.type = TYPES[3]
        if self.color == "white":
            self.symbol = '♗'
        else:
            self.symbol = '♝'

    def can_move(self, cur_row: int, cur_col: int, to_row: int, to_col: int) -> bool:
        # check if the move is diagonal
        if abs(to_row - cur_row) != abs(to_col - cur_col):
            return False

        # check if there are any pieces blocking the move
        row_direction = 1 if to_row > cur_row else -1
        col_direction = 1 if to_col > cur_col else -1
        row, col = cur_row + row_direction, cur_col + col_direction
        while row != to_row and col != to_col:
            if not self.board.is_empty(row, col):
                return False
            row += row_direction
            col += col_direction

        # check if the destination square is empty or contains an opponent's piece
        target_piece = self.board.get_piece(to_row, to_col)
        if target_piece is None or target_piece.color != self.color:
            return True

        return False

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return f"Bishop('{self.color}', {self.row}, {self.col})"


class Rook(Piece):
    def __init__(self, color: str, row: int, col: int, board: 'Board') -> None:
        super().__init__(color, row, col, board)
        self.type = TYPES[4]
        if self.color == "white":
            self.symbol = '♖'
        else:
            self.symbol = '♜'

    def can_move(self, cur_row: int, cur_col: int, to_row: int, to_col: int) -> bool:
        # check if out of bounds
        if not self.board.is_valid_coords(to_row, to_col):
            return False

        # check if trying to move diagonally
        if cur_row != to_row and cur_col != to_col:
            return False

        # check if there is any piece in the way
        if cur_row == to_row:
            # move horizontally
            start, end = (cur_col, to_col) if cur_col < to_col else (to_col, cur_col)
            for col in range(start + 1, end):
                if not self.board.is_empty(cur_row, col):
                    return False
        else:
            # move vertically
            start, end = (cur_row, to_row) if cur_row < to_row else (to_row, cur_row)
            for row in range(start + 1, end):
                if not self.board.is_empty(row, cur_col):
                    return False

        # check if destination is occupied by opposite color piece or is empty
        target_piece = self.board.get_piece(to_row, to_col)
        return target_piece is None or target_piece.color != self.color #

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return f"Rook('{self.color}', {self.row}, {self.col})"


class Queen(Piece):
    def __init__(self, color: str, row: int, col: int, board: 'Board') -> None:
        super().__init__(color, row, col, board)
        self.type = TYPES[5]
        if self.color == "white":
            self.symbol = '♕'
        else:
            self.symbol = '♛'

    def can_move(self, cur_row: int, cur_col: int, to_row: int, to_col: int) -> bool:
        # queen is moving in the same way as bishop or rook, so i use both logics combined
        bishop = Bishop(self.color, cur_row, cur_col, self.board)
        rook = Rook(self.color, cur_row, cur_col, self.board)
        return bishop.can_move(cur_row, cur_col, to_row, to_col) or rook.can_move(cur_row, cur_col, to_row, to_col)

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return f"Queen('{self.color}', {self.row}, {self.col})"


class King(Piece):
    def __init__(self, color: str, row: int, col: int, board: 'Board') -> None:
        super().__init__(color, row, col, board)
        self.type = TYPES[6]
        if self.color == "white":
            self.symbol = '♔'
        else:
            self.symbol = '♚'

    def can_move(self, cur_row: int, cur_col: int, to_row: int, to_col: int) -> bool:
        # king is actually moving by a square
        # so just checking if it's moving one square horizontally or vertically
        if abs(to_row - cur_row) <= 1 and abs(to_col - cur_col) <= 1:
            # check if destination is not occupied by a friendly piece
            target_piece = self.board.get_piece(to_row, to_col)
            if target_piece is None or target_piece.color != self.color:
                return True
        # no castling handler now.
        return False

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return f"King('{self.color}', {self.row}, {self.col})"
