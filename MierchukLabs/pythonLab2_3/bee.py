from cell import Cell
from math import sqrt
import random


class EmployedBee:
    """
    The 'EmployedBee' class represents a bee that can fly to a source cell,
    gather food, and upload the gathered food to a storage cell.

    Attributes:
    - 'food_capacity' (int): the maximum amount of food that the bee can carry.
    - 'food_gathered' (int): the amount of food that the bee has gathered so far.
    - 'cur_pos' (Cell): the current cell where the bee is located.

    Methods:
    - 'fly(self, src: Cell)': makes the bee fly to the given source cell, checking for overloading and emptiness.
    - 'gather(self)': makes the bee gather food from the current cell,
    if possible, and update its `food_gathered` attribute accordingly.
    - 'upload_food(self) -> int': makes the bee upload the gathered food to the current cell,
    and returns the amount of food uploaded.
    """

    def __init__(self, capacity: int):
        self.food_capacity = capacity
        self.food_gathered = 0
        self.cur_pos = None

    def fly(self, src: Cell):
        self.cur_pos = src

        if self.cur_pos.cur_load >= self.cur_pos.max_load:
            self.cur_pos.cur_load += 1
            raise ValueError("Source is overloaded")

        if self.cur_pos.val == 0:
            self.cur_pos.cur_load += 1
            raise ValueError("Empty!")

        self.cur_pos.cur_load += 1

    def gather(self):
        available_storage = self.food_capacity - self.food_gathered
        print(f"Available storage: {available_storage}, trying to gather source from cell ({self.cur_pos.x}; "
              f"{self.cur_pos.y}) with value {self.cur_pos.val}")

        if self.cur_pos.val <= available_storage:
            print("Bee can gather source")
            self.food_gathered += self.cur_pos.val
            self.cur_pos.val = 0
        else:
            print("Bee can't gather source")
            self.food_gathered += available_storage
            self.cur_pos.val -= available_storage

    def upload_food(self) -> int:
        self.cur_pos.cur_load -= 1
        food_gathered = self.food_gathered
        self.food_gathered = 0
        return food_gathered

    @property
    def food_capacity(self) -> int:
        return self.__food_capacity

    @food_capacity.setter
    def food_capacity(self, capacity: int):
        self.__food_capacity = capacity

    @property
    def food_gathered(self) -> int:
        return self.__food_gathered

    @food_gathered.setter
    def food_gathered(self, gathered: int):
        self.__food_gathered = gathered

    @property
    def cur_pos(self) -> Cell:
        return self.__cur_pos

    @cur_pos.setter
    def cur_pos(self, pos: Cell):
        self.__cur_pos = pos


class InspectorBee:
    """A class representing an inspector bee that checks the quality of a given food source.

    Args:
        food_gathered (int): The amount of food gathered from the source.

    Returns:
        Returns the quality of the food source.
        The value is calculated as a random number between 0 and 1,
        multiplied by the amount of food gathered, and divided by the distance to the source.
    """

    def check_src_quality(self, food_gathered: int, src: Cell) -> float:
        distance: float = sqrt(src.x ** 2 + src.y ** 2)

        return random.randint(0, 1) * food_gathered / distance