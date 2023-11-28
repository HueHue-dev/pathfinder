from abc import abstractmethod
from .node import Node


class Heuristic(object):

    @abstractmethod
    def get_distance(self, a: Node, b: Node) -> float:
        pass

    @abstractmethod
    def is_diagonal(self) -> bool:
        pass
