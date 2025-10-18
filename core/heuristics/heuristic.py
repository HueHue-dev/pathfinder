from abc import abstractmethod, ABC
from ..node import Node


class Heuristic(ABC):

    @abstractmethod
    def get_distance(self, a: Node, b: Node) -> float:
        pass

    @abstractmethod
    def is_diagonal(self) -> bool:
        pass
