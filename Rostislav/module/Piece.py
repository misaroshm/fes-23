
class Piece:
    def __str__(self):
        raise NotImplementedError("Subclass must implement abstract method")

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

class PieceFactory:
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