class Piece:
    valid_colors = ["white", "black"]
    valid_types = ["pawn", "rook", "knight", "bishop", "queen", "king"]

    @classmethod
    def create(cls, piece_type, color):
        if piece_type == "pawn":
            return Pawn(color)
        elif piece_type == "rook":
            return Rook(color)
        elif piece_type == "bishop":
            return Bishop(color)
        elif piece_type == "knight":
            return Knight(color)
        elif piece_type == "queen":
            return Queen(color)
        elif piece_type == "king":
            return King(color)
        else:
            return None

    def move(self, position):
        self.position = position

class Pawn(Piece):
    def __init__(self, color):
        self.color = color
    
    def __str__(self):
        return f"P"

    def get_possible_moves(self):
        pass


class Rook(Piece):
    def __init__(self, color):
        self.color = color
    
    def __str__(self):
        return f"R"

    def get_possible_moves(self):
        pass


class Knight(Piece):
    def __init__(self, color):
        self.color = color
    
    def __str__(self):
        return f"N"

    def get_possible_moves(self):
        pass


class Bishop(Piece):
    def __init__(self, color):
        self.color = color
    
    def __str__(self):
        return f"B"

    def get_possible_moves(self):
        pass


class Queen(Piece):
    def __init__(self, color):
        self.color = color
    
    def __str__(self):
        return f"Q"

    def get_possible_moves(self):
        pass


class King(Piece):
    def __init__(self, color):
        self.color = color
    
    def __str__(self):
        return f"K"

    def get_possible_moves(self):
        pass

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.grid[0][0] = Rook('white')
        self.grid[0][1] = Knight('white')
        self.grid[0][2] = Bishop('white')
        self.grid[0][3] = Queen('white')
        self.grid[0][4] = King('white')
        self.grid[0][5] = Bishop('white')
        self.grid[0][6] = Knight('white')
        self.grid[0][7] = Rook('white')

        for i in range(8):
            self.grid[1][i] = Pawn('white')
            self.grid[6][i] = Pawn('black')

        self.grid[7][0] = Rook('black')
        self.grid[7][1] = Knight('black')
        self.grid[7][2] = Bishop('black')
        self.grid[7][3] = Queen('black')
        self.grid[7][4] = King('black')
        self.grid[7][5] = Bishop('black')
        self.grid[7][6] = Knight('black')
        self.grid[7][7] = Rook('black')

    def draw(self):
        print("   A  B  C  D  E  F  G  H ")
        print(" +------------------------+")
        for row in range(8):
            print(f"{8-row}|", end="")
            for col in range(8):
                piece = self.grid[row][col]
                if piece is None:
                    print("  |", end="")
                else:
                    print(f" {piece}|", end="")
            print(f" {8-row}")
            print(" +------------------------+")
        print("   A  B  C  D  E  F  G  H ")
        print()

    def place_piece(self, piece, row, col):
        if not (0 <= row < 8 and 0 <= col < 8):
            return False
        if self.grid[row][col] is not None:
            return False
        self.grid[row][col] = piece
        return True

class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = 'white'

    def start(self):
        self.board.place_piece(Rook('white'), 0, 0)
        self.board.place_piece(Knight('white'), 0, 1)
        self.board.place_piece(Bishop('white'), 0, 2)
        self.board.place_piece(Queen('white'), 0, 3)
        self.board.place_piece(King('white'), 0, 4)
        self.board.place_piece(Bishop('white'), 0, 5)
        self.board.place_piece(Knight('white'), 0, 6)
        self.board.place_piece(Rook('white'), 0, 7)
        for col in range(8):
            self.board.place_piece(Pawn('white'), 1, col)
        self.board.place_piece(Rook('black'), 7, 0)
        self.board.place_piece(Knight('black'), 7, 1)
        self.board.place_piece(Bishop('black'), 7, 2)
        self.board.place_piece(Queen('black'), 7, 3)
        self.board.place_piece(King('black'), 7, 4)
        self.board.place_piece(Bishop('black'), 7, 5)
        self.board.place_piece(Knight('black'), 7, 6)
        self.board.place_piece(Rook('black'), 7, 7)

    def play(self):
        while True:
            self.board.draw()
            piece_type = input("Enter piece type: ")
            if piece_type == "exit":
                break
            elif piece_type not in Piece.valid_types:
                print("Invalid piece type. Try again.")
                continue

            color = input("Enter piece color (white/black): ")
            if color not in Piece.valid_colors:
                print("Invalid color. Try again.")
                continue

            piece = Piece.create(piece_type, color)
            if piece is None:
                print("Invalid piece type or color. Try again.")
                continue

            pos = input("Enter piece position (row, col): ")
            try:
                row, col = map(int, pos.replace(",", " ").split())
            except ValueError:
                print("Invalid position format. Try again.")
                continue

            print("Piece placed successfully.")

        print("Thanks for playing!")
        
game = Game()
game.play()
