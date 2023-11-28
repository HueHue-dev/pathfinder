from .heuristic import Heuristic
from .node import Node


class Manhattan(Heuristic):
    def is_diagonal(self) -> bool:
        return False

    def get_distance(self, a: Node, b: Node) -> float:
        dx = abs(a.x - b.x)
        dy = abs(a.y - b.y)

        return dx + dy
