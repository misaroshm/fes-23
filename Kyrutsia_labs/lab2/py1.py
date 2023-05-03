import functools
import math
from math import sqrt
import random
from random import randint
from Conf import Configs

class InspectorBee:
    def __init__(self, employed_bees, sources):
        self.employed_bees = employed_bees
        self.sources = sources
        self.processed_sources = []

    def check_quality(self):
        for source in self.sources:
            if source in self.processed_sources:
                continue
            total_food = sum([bee.food_amount for bee in self.employed_bees if bee.current_source == source])
            source_quality = random.random() * total_food / 12
            if source_quality > 1:
                source_quality = 1
            elif source_quality < 0:
                source_quality = 0
            if source_quality >= 0:
                self.send_more_employed_bees(source)
            self.processed_sources.append(source)

    def send_more_employed_bees(self, source):
        num_new_bees = random.randint(1, 5)
        for i in range(num_new_bees):
            food_amount = random.randint(1, source[1])
            self.employed_bees.append(EmployedBee(food_amount, source))

    def distance(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2[0]
        return sqrt(((x2 - x1)**2 + (y2 - y1)**2))



class Hive:
    def __init__(self, food_bank):
        self.food_bank = food_bank

    def upload_food(self, food_amount):
        self.food_bank += food_amount


class EmployedBee:
    def __init__(self, food_amount, current_source=None):
        self.food_amount = food_amount
        self.current_source = current_source

    def fly(self, source):
        self.current_source = source

    def gather(self):
        return self.food_amount


class Playground:
    def __init__(self):
        self.employed_bees = None
        self.food_sources = None
        self.coordinate_grid = None
        self.height = Configs.SEARCH_REGION_HEIGHT
        self.width = Configs.SEARCH_REGION_WIDTH
        self.sources = Configs.SOURCES
        self.colony_size = Configs.COLONY_SIZE
        self.distance = 0
        self.food_capacity_max = Configs.FOOD_CAPACITY_MAX
        self.food_capacity_min = Configs.FOOD_CAPACITY_MIN
        self.employed_agents = Configs.EMPLOYED_AGENTS
        self.onlooker_agents = Configs.ONLOOKER_AGENTS
        self.food_bank = 0

        self.generate_coordinate_grid()
        self.generate_food_sources()
        self.create_bees()

    def generate_coordinate_grid(self):
        self.coordinate_grid = []
        for i in range(self.width):
            for j in range(self.height):
                self.coordinate_grid.append((i, j))

    def generate_food_sources(self):
        self.food_sources = []
        num_sources = self.sources
        for i in range(num_sources):
            x, y = random.sample(self.coordinate_grid, 1)[0]
            v = random.randint(self.food_capacity_min, self.food_capacity_max)
            self.food_sources.append(((x, y), v))
        return self.food_sources

    def create_bees(self):
        self.employed_bees = []
        for i in range(self.employed_agents):
            food_amount = random.randint(self.food_capacity_min, self.food_capacity_max)
            self.employed_bees.append(EmployedBee(food_amount))

    def run(self):
        iteration = 0
        while any(source[1] > 0 for source in
                  self.food_sources) and self.food_bank < Configs.FOOD_CAPACITY_MAX * Configs.SOURCES:
            inspector = InspectorBee(self.employed_bees, self.food_sources)
            inspector.check_quality()

            for source in self.food_sources:
                food = source[1]
                for bee in self.employed_bees:
                    if bee.current_source == source:
                        bee_food = bee.gather()
                        food -= bee_food
                        self.food_bank += bee_food
                        self.distance += InspectorBee.distance(self, bee.current_source[iteration], self.food_sources[iteration+1])
                source = (source[0], food)
            iteration += 1

        print(
            f"All food sources have been exhausted. \nTotal food gathered: "
            f"{self.food_bank}, \nTotal distance traveled: "
            f"{self.distance}")
