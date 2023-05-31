"""Holds agents definition and base functionality"""

import random
from typing import Tuple, List

from searchregion import Playground
from configs import Configs


class Inspector:
    """Checks quality of each food using priority formulae in function self.define_priority(self)"""
    def __init__(self, resources: List[int]) -> None:
        self.resources = resources

    def define_priority(self) -> List[int]:
        # using dist formulae, return ordered resources
        priorities = []
        for resource in self.resources:
            priority = resource * random.random()   # random.random() generates random value in range (0, 1]
            priorities.append(priority)
    
        ordered_resources = [res for _, res in sorted(zip(priorities, self.resources), reverse=True)]
        return ordered_resources

class EmployedBee:
    """Represents bee subject.
    """
    STATUSES = ("ON_DUTY", "PENDING")

    def __init__(self, id: int, food_amount: int,
                 position: Tuple[int, int] = (0, 0)) -> None:
        """Docstring"""
        self.id = id
        self.food_amount = food_amount
        self.position = position
        self.next_position = position
        self.resource = 0
        self.status = EmployedBee.STATUSES[0]

    def fly(self, position: Tuple[int, int], search_space: Playground) -> None:
        """Moves agent to <position> coordinates.

        Args:
            position (Tuple[int, int]): specifies new position
                of agent
            search_space (Playground): discovering space.
        Returns:
            None.
        """
        if self._check_position_source(position=position,
                                       searchreg=search_space):
            self.position = position
            print(f"Agent {self.id} has flew to new position {position}")
        else:
            raise ValueError("Provided position does not contain source.")

    @staticmethod
    def _check_position_source(position: Tuple[int, int], searchreg: Playground) -> bool:
        """Checks if Playground has the source in provided position"""
        if searchreg.sources.get(position):
            return True
        else:
            return False

    def gather(self, searchreg: Playground) -> None:
        """Docstring"""
        resource = searchreg.collect(self.position, self.food_amount)
        self.resource += resource


class Hive:
    def __init__(self, playground: Playground):
        """docstring"""
        self.resource_bank = []
        self.agent_number = Configs.COLONY_SIZE
        self.employed_bees = []
        self.playground = playground

    def create_agents(self) -> None:
        self.employed_bees.extend([EmployedBee(id=i+1, food_amount=random.randint(3, 7))
                                   for i in range(self.agent_number)])

    def set_resource_priority(self, employed_bees: List[EmployedBee]):
        """
        1. From each worker we obtain collected resources
        2. Using inspector object prioritize resources to gather: s[10], s[6], s[2], ... .., s[20]
        3. Distribute prioritized sources on workers s[10]: workers[0, 1, 2], s[6]: workers[3, 4, 5], ...
        """
        for bee in employed_bees:
            self.resource_bank.append(bee.resource)
            bee.resource = 0

        some_inspector = Inspector(self.resource_bank)   # some inspector that defines priority
        ordered_resources = some_inspector.define_priority()

        for i, resource in enumerate(ordered_resources):
            bee_id = i % len(employed_bees)
            employed_bees[bee_id].resource += resource

    def initialize_all(self):
        self.create_agents()

    def run(self):
        while self.playground.not_empty():
            for bee in self.employed_bees:
                bee.fly(bee.next_position, self.playground)
                bee.gather(self.playground)
                bee.next_position()
