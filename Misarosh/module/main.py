
from game import Game

chessboard = Game()
chessboard.draw_chessboard()

while True:
    if not chessboard.undo_flag:
        start = input("White start: ")
        if start == 'undo':
            chessboard.undo()
            chessboard.undo_flag = True

            chessboard.draw_chessboard()
            continue
        end = input("White end: ")

        while not chessboard.move(start, end, 'W'):
            start = input("White start: ")
            if start == 'undo':
                chessboard.undo()
                chessboard.undo_flag = True
                chessboard.draw_chessboard()
                continue
            end = input("White end: ")
        if chessboard.check_if_king_under_attack('W'):
            print("White is under attack")
            chessboard.undo()

        chessboard.draw_chessboard()

    chessboard.undo_flag = False
    start = input("Black start: ")
    if start == 'undo':
        chessboard.undo()
        chessboard.draw_chessboard()
        continue
    end = input("Black end: ")

    while not chessboard.move(start, end, 'B'):
        start = input("Black start: ")
        if start == 'undo':
            chessboard.undo()
            chessboard.draw_chessboard()
            continue
        end = input("Black end: ")

    if chessboard.check_if_king_under_attack('B'):
        print("Black is under attack")
        chessboard.undo()
        chessboard.undo_flag = True

    chessboard.draw_chessboard()
