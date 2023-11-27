from abc import abstractmethod
from .cell import Cell


class Heuristic(object):

    @abstractmethod
    def get_distance(self, a: Cell, b: Cell) -> float:
        pass

    @abstractmethod
    def is_diagonal(self) -> bool:
        pass
