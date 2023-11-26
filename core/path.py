from .cell import Cell


class Path:
    def __init__(self):
        self.__path = []

    def add(self, cell: Cell):
        self.__path.append(cell)

    def get_path(self):
        return self.__path
