class PieceType:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class PieceFactory:
    def __init__(self):
        self.types = {}

    def register(self, name, value):
        self.types[name] = PieceType(name, value)

    def create(self, name):
        return Piece(name, self.types[name])


class Piece:
    def __init__(self, name, piece_type):
        self.name = name
        self.type = piece_type

    def __str__(self):
        return f"{self.name} ({self.type.name}, {self.type.value})"


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]

    def place(self, piece, x, y):
        if self.grid[y][x] is not None:
            return False
        self.grid[y][x] = piece
        return True

    def __str__(self):
        return '\n'.join([' '.join([str(p) if p is not None else '-' for p in row]) for row in self.grid])


class Game:
    def __init__(self, piece_factory):
        self.board = Board(8, 8)
        self.piece_factory = piece_factory

    def play(self):
        pawn1 = self.piece_factory.create("Pawn")
        pawn2 = self.piece_factory.create("Pawn")
        bishop = self.piece_factory.create("Bishop")
        self.board.place(pawn1, 1, 0)
        self.board.place(pawn2, 2, 0)
        self.board.place(bishop, 2, 1)
        print(self.board)


piece_factory = PieceFactory()
piece_factory.register("Pawn", 1)
piece_factory.register("Bishop", 3)

game = Game(piece_factory)
game.play()
