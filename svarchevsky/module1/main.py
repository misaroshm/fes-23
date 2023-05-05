#from game import Game1

#there must be cycle and i now what to do there, but i do not finished all pieces logic for now.
#g = Game() # this obje

#the things below are temporary, and they work for now

from board import Board

#mapping
let_num = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

t = Board()

"""
while True:
    print(t)
    x_select, y_select = [int(x) for x in input("X; Y: ").split()]
    x_to, y_to = [int(x) for x in input("X_TO; Y_TO: ").split()]
    t.move_piece_if_to_is_valid(x_select, y_select, x_to, y_to)
"""

while True:
    print(t)
    from_pos = input("From (format e.g. a2 or h3  etc.): ")
    to_pos = input("To: ")
    y_select, x_select = let_num[from_pos[0]], int(from_pos[1])
    y_to, x_to = let_num[to_pos[0]], int(to_pos[1])

    t.move_piece_if_to_is_valid(x_select, y_select, x_to, y_to)