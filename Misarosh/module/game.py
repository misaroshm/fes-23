import copy

from board import Board


class Game(Board):

    def move(self, start, end, color):
        global start_x, end_x
        start = start.upper()
        end = end.upper()
        try:
            # Preventing incorrect notation
            if start[0] == 'A':
                start_x = 0
            elif start[0] == 'B':
                start_x = 1
            elif start[0] == 'C':
                start_x = 2
            elif start[0] == 'D':
                start_x = 3
            elif start[0] == 'E':
                start_x = 4
            elif start[0] == 'F':
                start_x = 5
            elif start[0] == 'G':
                start_x = 6
            elif start[0] == 'H':
                start_x = 7
            else:
                print('Impossible move!')

            if end[0] == 'A':
                end_x = 0
            elif end[0] == 'B':
                end_x = 1
            elif end[0] == 'C':
                end_x = 2
            elif end[0] == 'D':
                end_x = 3
            elif end[0] == 'E':
                end_x = 4
            elif end[0] == 'F':
                end_x = 5
            elif end[0] == 'G':
                end_x = 6
            elif end[0] == 'H':
                end_x = 7
            else:
                print('Impossible move!')

            start_y = 8 - int(start[1])
            end_y = 8 - int(end[1])

            start_tuple = (start_x, start_y)
            end_tuple = (end_x, end_y)

            if self.check_if_legal(start_tuple, end_tuple, color):
                self.previous_board = copy.deepcopy(self.board)
                # Checking if the pawn is on the last row
                if self.board[start_tuple[1]][start_tuple[0]][0] == 6 and end_tuple[1] == 0:
                    self.board[end_tuple[1]][end_tuple[0]] = (4, color)
                elif self.board[start_tuple[1]][start_tuple[0]][0] == 6 and end_tuple[1] == 7:
                    self.board[end_tuple[1]][end_tuple[0]] = (4, color)
                else:
                    self.board[end_y][end_x] = self.board[start_y][start_x]
                self.board[start_y][start_x] = (0, 0)
            else:
                print('Impossible move!')
                return False
        except:
            print('Wrong move!')
            return False
        return True

    def check_if_piece(self, start, end, color):
        # Checking if a piece is in the way
        y_move = end[1] - start[1]
        x_move = end[0] - start[0]
        if x_move == 0:
            if y_move > 0:
                for i in range(start[1] + 1, end[1] + 1):
                    if self.board[i][start[0]][0] != 0 and self.board[i][start[0]][1] == color:
                        return False
                    elif self.board[i][start[0]][0] != 0 and i != end[1]:
                        return False
                return True
            else:
                for i in range(start[1] - 1, end[1] - 1, -1):
                    if self.board[i][start[0]][0] != 0 and self.board[i][start[0]][1] == color:
                        return False
                    elif self.board[i][start[0]][0] != 0 and i != end[1]:
                        return False
                return True
        elif y_move == 0:
            if x_move > 0:
                for i in range(start[0] + 1, end[0] + 1):
                    if self.board[start[1]][i][0] != 0 and self.board[start[1]][i][1] == color:
                        return False
                    elif self.board[start[1]][i][0] != 0 and i != end[0]:
                        return False
                return True
            else:
                for i in range(start[0] - 1, end[0] - 1, -1):
                    if self.board[start[1]][i][0] != 0 and self.board[start[1]][i][1] == color:
                        return False
                    elif self.board[start[1]][i][0] != 0 and i != end[0]:
                        return False
                return True
        elif abs(x_move) == abs(y_move):
            if x_move > 0:
                if y_move > 0:
                    for i in range(1, x_move + 1):
                        if self.board[start[1] + i][start[0] + i][0] != 0 and self.board[start[1] + i][start[0] + i][
                            1] == color:
                            return False
                        elif self.board[start[1] + i][start[0] + i][0] != 0 and i != x_move:
                            return False
                    return True
                else:
                    for i in range(1, x_move + 1):
                        if self.board[start[1] - i][start[0] + i][0] != 0 and self.board[start[1] - i][start[0] + i][
                            1] == color:
                            return False
                        elif self.board[start[1] - i][start[0] + i][0] != 0 and i != x_move:
                            return False
                    return True
            else:
                if y_move > 0:
                    for i in range(1, abs(x_move) + 1):
                        if self.board[start[1] + i][start[0] - i][0] != 0 and self.board[start[1] + i][start[0] - i][
                            1] == color:
                            return False
                        elif self.board[start[1] + i][start[0] - i][0] != 0 and i != abs(x_move):
                            return False
                    return True
                else:
                    for i in range(1, abs(x_move) + 1):
                        if self.board[start[1] - i][start[0] - i][0] != 0 and self.board[start[1] - i][start[0] - i][
                            1] == color:
                            return False
                        elif self.board[start[1] - i][start[0] - i][0] != 0 and i != abs(x_move):
                            return False
                    return True
        else:
            return False

    def check_if_under_attack(self, end, color):
        # Checking if the end position is under attack
        for j in range(8):
            for i in range(8):
                y = 7 - j
                x = i
                if self.board[y][x][1] != color:
                    if self.check_if_legal((x, y), end, self.board[y][x][1]):
                        return True
                        print('Would be under attack!')

        return False

    def check_if_king_under_attack(self, color):
        if color == 'W':
            if self.check_if_under_attack(self.white_king_pos, color):
                return True
        else:
            if self.check_if_under_attack(self.black_king_pos, color):
                return True

    # Checking if a move is legal for each piece
    def check_if_legal(self, start, end, color):
        y_move = end[1] - start[1]
        x_move = end[0] - start[0]

        if start == end:
            return False

        # Checking boundaries
        elif 7 < start[0] < 0 or 7 < start[1] < 0 or 7 < end[0] < 0 or 7 < end[1] < 0:
            return False

        # Checking if correct color is being moved
        elif self.board[start[1]][start[0]][1] != color:
            return False

        # Checking of starting position isn't empty
        elif self.board[start[1]][start[0]][0] == 0:
            return False

        # Checking if the move is right for a Rook
        elif self.board[start[1]][start[0]][0] == 1:
            if start[0] - end[0] != 0 and start[1] - end[1] != 0:
                return False
            elif self.check_if_piece(start, end, color):
                return True
            else:
                return False

        # Checking if the move is right for a Knight
        elif self.board[start[1]][start[0]][0] == 2:
            if 0 <= y_move + 2 < len(self.knight_move_matrix) and 0 <= x_move + 2 < len(self.knight_move_matrix[0]):
                if self.knight_move_matrix[2 + y_move][2 + x_move] == 1:
                    return True
            else:
                return False

        # Checking if the move is right for a Bishop
        elif self.board[start[1]][start[0]][0] == 3:
            if abs(y_move) == abs(x_move) and x_move != 0:
                if self.check_if_piece(start, end, color):
                    return True
                else:
                    return False
            else:
                return False

        # Checking if the move is right for the Queen
        elif self.board[start[1]][start[0]][0] == 4:
            if (abs(y_move) == abs(x_move) and x_move != 0) or start[0] - end[0] == 0 or start[1] - end[1] == 0:
                if self.check_if_piece(start, end, color):
                    return True
                else:
                    return False
            else:
                return False

        # Cheking if the move is right for the King
        elif self.board[start[1]][start[0]][0] == 5:
            if abs(x_move) <= 1 and abs(y_move) <= 1:
                # Checking if the end position is under attack
                if self.check_if_under_attack(end, color):
                    return False
                elif self.check_if_piece(start, end, color):
                    if color == 'W':
                        self.white_king = end
                    else:
                        self.black_king = end
                    return True
                else:
                    return False

            else:
                return False

        # Checking if the move is right for a Pawn
        elif self.board[start[1]][start[0]][0] == 6:
            if self.board[start[1]][start[0]][1] == 'W':
                if 8 - start[1] == 2:
                    if x_move == 0:
                        if 2 >= -y_move > 0 == self.board[end[1]][end[0]][0]:
                            return True
                        else:
                            return False
                    elif abs(x_move) == 1 and -y_move == 1:
                        if self.board[end[1]][end[0]][0] != 0:
                            return True
                        else:
                            return False
                else:
                    if x_move == 0:
                        if 1 >= -y_move > 0 == self.board[end[1]][end[0]][0]:
                            return True
                        else:
                            return False
                    elif abs(x_move) == 1 and -y_move == 1:
                        if self.board[end[1]][end[0]][0] != 0:
                            return True
                        else:
                            return False
            if self.board[start[1]][start[0]][1] == 'B':
                if 8 - start[1] == 7:
                    if x_move == 0:
                        if -2 <= -y_move < 0 == self.board[end[1]][end[0]][0]:
                            return True
                        else:
                            return False
                    elif abs(x_move) == 1 and -y_move == -1:
                        if self.board[end[1]][end[0]][0] != 0:
                            return True
                        else:
                            return False
                else:
                    if x_move == 0:
                        if -1 <= -y_move < 0 == self.board[end[1]][end[0]][0]:
                            return True
                        else:
                            return False
                    elif abs(x_move) == 1 and -y_move == -1:
                        if self.board[end[1]][end[0]][0] != 0:
                            return True
                        else:
                            return False
        else:
            return True

    def undo(self):
        self.board = self.previous_board