import random
from typing import List, Tuple
from configs import Configs


class Playground:
    """Represents search space for bee colony"""

    def __init__(self) -> None:
        # {source[j]: v, ...}
        self.field = Playground.generate()
        self.sources = self.generate_sources()

    def collect(self, position: Tuple[int, int], capacity: int) -> int:
        """! interface between Hive and Playground!"""
        if self.sources[position] >= capacity:
            self.sources[position] -= capacity
            return capacity
        else:
            to_return = self.sources[position]
            self.sources[position] = 0
            return to_return

    def not_empty(self) -> bool:
        if all(r for _, r in self.sources.items()) > 0:
            return True
        else:
            return False

    @staticmethod
    def generate() -> List[List]:
        """Generates integer coordinates for field"""
        matrix = list()
        for i in range(Configs.SEARCH_REGION_HEIGHT):
            for j in range(Configs.SEARCH_REGION_WIDTH):
                matrix.append([i, j])
        return matrix

    def generate_sources(self):
        """"""
        coords = random.sample(self.field, Configs.SOURCES)
        sources = {tuple(k): random.randint(50, 200) for k in coords}

        return sources

