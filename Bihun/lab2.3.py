import random
import math

class Bee:
    def __init__(self, name, post):
        self.name = name
        self.nectar_amount = 0 # Початкова кількість нектару
        self.max_amount = 7 # Максимальна кількість нектару, яку бджола може зібрати
        self.post = post # Початкова позиція бджоли

    def fly(self, post):
        self.post = post  # Зміна позиції бджоли на нову задану позицію
        print(self.post)

    def gather(self, source):
        test = source[self.post] - self.max_amount
        if test >= 0:
            source[self.post] = test
            self.nectar_amount = test
            print('Зібрано їжу з', self.post, self.nectar_amount)
        else:
            self.nectar_amount = source[self.post]
            source[self.post] = 0
            print("Not at the right source.")

    def fly_beek(self, hive):
        self.post = (0, 0)  # Полетіти назад до вулика
        hive[1] += self.nectar_amount # Додати нектар, зібраний бджолою, до загальної кількості нектару вулика
        self.nectar_amount = 0 # Скинути нектар, який зібрала бджола
        print(self.post)


class InspectorBee(Bee):
    def __init__(self, name, post):
        super().__init__(name, post)

    @staticmethod
    def calculate_distance(post1, post2):
        x1, y1 = post1
        x2, y2 = post2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) # Обчислення відстані між двома позиціями

    @staticmethod
    def calculate_quality(food_amount, distance):
        return random.random() * (food_amount / distance)

    def find_highest_quality_source(self, sources, employed_bees):
        max_quality = float('-inf')
        best_source = None

        for post, food_amount in sources.items():
            taken_food = sum([bee.nectar_amount for bee in employed_bees])  # Обчислює загальну кількість зібраного нектару іншими бджолами
            distance = self.calculate_distance(post, (0, 0))
            quality = self.calculate_quality(taken_food, distance)

            if quality > max_quality:
                max_quality = quality
                best_source = post

        return best_source

    def send_more_bees(self, sources, employed_bees):
        best_source = self.find_highest_quality_source(sources, employed_bees)
        if best_source:
            for bee in employed_bees:
                bee.fly(best_source)
        else:
            print("Немає доступних джерел для відправки додаткових бджіл.")

source = {(10, 10): 200}
hive = {1: 0}
bee = Bee(name="bee #1", post=(0, 0))
employed_bees = [bee]
inspector_bee = InspectorBee(name="inspector bee", post=(0, 0)) # Створює інспекторську бджолу з ім'ям "інспектор бджола" та початковою позицією (0, 0)

while source.get((10, 10), 0) > 0:
    bee.fly((10, 10)) # Заставляє бджолу полетіти до координатів (10, 10)
    bee.gather(source) # Заставляє бджолу збирати з джерела
    bee.fly_beek(hive) # Заставляє бджолу повернутися до вулика
    inspector_bee.send_more_bees(source, employed_bees)













