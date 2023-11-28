import numpy as np
from .heuristic import Heuristic
from ..node import Node


class Euclidean(Heuristic):
    def is_diagonal(self) -> bool:
        return True

    def get_distance(self, a: Node, b: Node):
        dx = abs(a.x - b.x)
        dy = abs(a.y - b.y)

        return np.sqrt(dx * dx + dy * dy)
