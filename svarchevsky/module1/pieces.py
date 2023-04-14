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
        # TODO: knight logic here
        # get_all_
        return True

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
        # TODO: bishop logic here
        return True

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
        # TODO: rook logic here
        return True

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
        # TODO: queen logic here
        return True

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
        # TODO: king logic here
        return True

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return f"King('{self.color}', {self.row}, {self.col})"
