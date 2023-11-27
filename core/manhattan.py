from .heuristic import Heuristic
from .cell import Cell


class Manhattan(Heuristic):
    def is_diagonal(self) -> bool:
        return False

    def get_distance(self, a: Cell, b: Cell) -> float:
        dx = abs(a.x - b.x)
        dy = abs(a.y - b.y)

        return dx + dy
