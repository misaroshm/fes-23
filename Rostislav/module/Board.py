
class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def place_piece(self, piece, row, col):
        self.board[row][col] = piece

    def __str__(self):
        result = ""
        for row in range(8):
            for col in range(8):
                if self.board[row][col] is not None:
                    result += str(self.board[row][col])
                else:
                    result += "."
            result += "\n"
        return result
