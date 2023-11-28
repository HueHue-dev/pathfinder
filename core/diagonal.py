import numpy as np
from .heuristic import Heuristic
from .node import Node


class Diagonal(Heuristic):
    def is_diagonal(self) -> bool:
        return True

    def get_distance(self, a: Node, b: Node):
        dx = abs(a.x - b.x)
        dy = abs(a.y - b.y)
        d2 = 1

        return np.max([dx, dy]) + d2 + np.min([dx, dy])
