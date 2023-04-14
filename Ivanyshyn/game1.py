import os


class Piece:

    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.name = name
        self.color = color
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect

    def set_texture(self):
        self.texture = os.path.join(
            f'../assets/images/imgs-80px/{self.color}_{self.name}.png')


class Pawn(Piece):

    def __init__(self, color):
        super().__init__('pawn', color, 1.0)


class Knight(Piece):

    def __init__(self, color):
        super().__init__('knight', color, 3.0)


class Bishop(Piece):

    def __init__(self, color):
        super().__init__('bishop', color, 3.001)


class Rook(Piece):

    def __init__(self, color):
        super().__init__('rook', color, 5.0)


class Queen(Piece):

    def __init__(self, color):
        super().__init__('queen', color, 9.0)


class King(Piece):

    def __init__(self, color):
        super().__init__('king', color, 10000.0)


class PieceFactory:

    @staticmethod
    def create_piece(name, color):
        if name == 'pawn':
            return Pawn(color)
        elif name == 'knight':
            return Knight(color)
        elif name == 'bishop':
            return Bishop(color)
        elif name == 'rook':
            return Rook(color)
        elif name == 'queen':
            return Queen(color)
        elif name == 'king':
            return King(color)
        else:
            raise ValueError(f'Invalid piece name: {name}')


class Square:

    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece

    def __repr__(self):
        return f"Square({self.row}, {self.col}, {self.piece})"

    def has_piece(self):
        return self.piece is not None

