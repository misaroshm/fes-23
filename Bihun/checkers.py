#Основний клас, який ми будемо використовувати для створення наших класів Factory
#він дозволяє створювати об'єкти, не вказуючи конкретного класу
#a використовуючи методи фабрики
class Factory:
    def create_object(self):
        pass
#Клас Дошка  має метод для створення і розміщення фігур на дошці,
#а також метод для виведення стану дошки на екран
class Board:
    def __init__(self):
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.create_figures()

    def create_figures(self):
        for i in range(8):
            for j in range(8):
                if i < 3 and (i + j) % 2 == 0:
                    self.board[i][j] = Factory.create_object("black")
                elif i > 4 and (i + j) % 2 == 0:
                    self.board[i][j] = Factory.create_object("white")

    def show_board(self):
        for i in range(8):
            for j in range(8):
                print(self.board[i][j], end="")
            print()
#Клас Фігура має метод для перевірки можливості ходу,
#а також методи для переміщення фігур по дошці
class Figure:
    def __init__(self, color):
        self.color = color
        self.is_king = False

    def can_move(self, x1, y1, x2, y2):
        pass

    def move(self, x1, y1, x2, y2):
        pass

class Checker(Figure):
    def __init__(self, color):
        super().__init__(color)

    def can_move(self, x1, y1, x2, y2):
        pass

    def move(self, x1, y1, x2, y2):
        pass

class King(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.is_king = True

    def can_move(self, x1, y1, x2, y2):
        pass

    def move(self, x1, y1, x2, y2):
        pass
#Клас Гра має метод для керування ходами гравців і визначення переможця
class Game:
    def __init__(self):
        self.board = Board()
        self.turn = "white"

    def play(self):
        while not self.game_over():
            self.board.show_board()
            x1, y1, x2, y2 = self.get_move()
            self.make_move(x1, y1, x2, y2)
            self.change_turn()

        print("Game over")

    def get_move(self):
        pass

    def make_move(self, x1, y1, x2, y2):
        pass

    def change_turn(self):

        class Game:
            def __init__(self):
                self.board = Board()
                self.turn = "white"

            def play(self):
                while not self.game_over():
                    self.board.show_board()
                    x1, y1, x2, y2 = self.get_move()
                    self.make_move(x1, y1, x2, y2)
                    self.change_turn()

                print("Game over")

            def get_move(self):
                # Реалізуйте метод для отримання ходу від користувача
                pass

            def make_move(self, x1, y1, x2, y2):
                # Перевірка можливості ходу
                if not self.board.board[x1][y1].can_move(x1, y1, x2, y2):
                    print("Invalid move")
                    return

                # Виконання ходу
                self.board.board[x2][y2] = self.board.board[x1][y1]
                self.board.board[x1][y1] = 0

                # Перетворення на короля, якщо необхідно
                if isinstance(self.board.board[x2][y2], Checker):
                    if self.turn == "white" and x2 == 0:
                        self.board.board[x2][y2] = King("white")
                    elif self.turn == "black" and x2 == 7:
                        self.board.board[x2][y2] = King("black")

            def change_turn(self):
                # Зміна ходу
                self.turn = "black" if self.turn == "white" else "white"

            def game_over(self):
                # Реалізуйте метод для перевірки закінчення гри
                pass
