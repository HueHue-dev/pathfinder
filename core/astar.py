import numpy as np
from .cell import Cell
from .path import Path


class AStar:
    def __init__(self):
        self.__open_list = []
        self.__closed_list = []
        self.__path = Path()
        self.distance_modes = [
            'Manhattan',
            'Diagonal',
            'Euclidean',
        ]
        self.distance_mode = self.get_manhattan_mode()

    def search(self, board) -> Path:
        self.__open_list.append(board.start_cell)
        while len(self.__open_list) > 0:
            lowest_index = 0
            for i, cell in enumerate(self.__open_list):
                if cell.f < self.__open_list[lowest_index].f:
                    lowest_index = i

            current_cell = self.__open_list[lowest_index]

            if current_cell.is_target:
                temp = current_cell
                while isinstance(temp.previous, Cell):
                    self.__path.add(temp.previous)
                    temp = temp.previous
                return self.__path

            self.__open_list.remove(current_cell)
            self.__closed_list.append(current_cell)

            for neighbor in current_cell.neighbors:
                if neighbor in self.__closed_list:
                    continue

                neighbor.g = current_cell.g + 1

                neighbor.h = self.__get_distance(self.distance_mode, neighbor, board.target_cell)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.previous = current_cell

                if neighbor not in self.__open_list:
                    self.__open_list.append(neighbor)

    def get_closed_list(self):
        return self.__closed_list

    def get_open_list(self):
        return self.__open_list

    def reset(self):
        self.__open_list = []
        self.__closed_list = []
        self.__path = Path()

    def get_manhattan_mode(self):
        return self.distance_modes[0]

    def get_diagonal_mode(self):
        return self.distance_modes[1]

    def get_euclidean_mode(self):
        return self.distance_modes[2]

    def __get_distance(self, mode, a: Cell, b: Cell) -> float:
        if mode == self.get_manhattan_mode():
            return self.get_manhattan_distance(a, b)
        if mode == self.get_diagonal_mode():
            return self.get_diagonal_distance(a, b)
        if mode == self.get_euclidean_mode():
            return self.get_euclidean_distance(a, b)

    def mode_is_diagonal(self) -> bool:
        return self.distance_mode != self.get_manhattan_mode()

    @staticmethod
    def get_manhattan_distance(a: Cell, b: Cell) -> float:
        dx = abs(a.x - b.x)
        dy = abs(a.y - b.y)

        return dx + dy

    @staticmethod
    def get_euclidean_distance(a: Cell, b: Cell) -> float:
        dx = abs(a.x - b.x)
        dy = abs(a.y - b.y)

        return np.sqrt(dx * dx + dy * dy)

    @staticmethod
    def get_diagonal_distance(a: Cell, b: Cell) -> float:
        dx = abs(a.x - b.x)
        dy = abs(a.y - b.y)
        d2 = 1
        return np.max([dx, dy]) + d2 + np.min([dx, dy])
