#from game import Game

#there must be cycle and i now what to do there, but i do not finished all pieces logic for now.
#g = Game() # this obje

#the things below are temporary, and they work for now

from board import Board

#let_num = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

t = Board()

while True:
    print(t)
    x_select, y_select = [int(x) for x in input("X; Y: ").split()]
    x_to, y_to = [int(x) for x in input("X_TO; Y_TO: ").split()]
    t.move_piece_if_to_is_valid(x_select, y_select, x_to, y_to)
