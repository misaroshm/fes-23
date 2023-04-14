from Board import Board 
from Piece import PieceFactory


class Game:
    def __init__(self):
        self.board = Board()
        self.piece_factory = PieceFactory()

    def setup(self):
       
        for col, piece_type in enumerate("RNBQKBNR"):
            self.board.place_piece(self.piece_factory.create_piece(piece_type), 0, col)
        for col in range(8):
            self.board.place_piece(self.piece_factory.create_piece("P"), 1, col)

        
        for col, piece_type in enumerate("RNBQKBNR"):
            self.board.place_piece(self.piece_factory.create_piece(piece_type), 7, col)
        for col in range(8):
            self.board.place_piece(self.piece_factory.create_piece("P"), 6, col)

    def play(self):
        print(self.board)

game = Game()
game.setup()
game.play()
