from const import COLS, ROWS
from piece import PieceFactory


class Board:

    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for _ in range(COLS)]

        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def _create(self):
        # Створюємо квадрати дошки
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        # Визначаємо рядок, на якому будуть розташовані пішаки та інші фігури
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)

        # Створюємо фабрику фігур
        factory = PieceFactory()

        # Додаємо пішаків
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, factory.create_piece('pawn', color))

        # Додаємо коней
        self.squares[row_other][1] = Square(row_other, 1, factory.create_piece('knight', color))
        self.squares[row_other][6] = Square(row_other, 6, factory.create_piece('knight', color))

        # Додаємо слонів
        self.squares[row_other][2] = Square(row_other, 2, factory.create_piece('bishop', color))
        self.squares[row_other][5] = Square(row_other, 5, factory.create_piece('bishop', color))

        # Додаємо турів
        self.squares[row_other][0] = Square(row_other, 0, factory.create_piece('rook', color))
        self.squares[row_other][7] = Square(row_other, 7, factory.create_piece('rook', color))

        # Додаємо ферзя
        self.squares[row_other][3] = Square(row_other, 3, factory.create_piece('queen', color))

        # Додаємо короля
        self.squares[row_other][4] = Square(row_other, 4, factory.create_piece('king', color))
