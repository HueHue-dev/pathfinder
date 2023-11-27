from .diagonal import Diagonal
from .manhattan import Manhattan
from .euclidean import Euclidean


class HeuristicFactory:
    heuristics = {
        'Manhattan': Manhattan(),
        'Diagonal': Diagonal(),
        'Euclidean': Euclidean(),
    }

    def get_heuristic(self, heuristic='Manhattan'):
        return self.heuristics[heuristic]

    @staticmethod
    def get_default() -> str:
        return 'Manhattan'
