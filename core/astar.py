import math
from .cell import Cell
from .path import Path


class AStar:
    def __init__(self):
        self.__open_list = []
        self.__closed_list = []
        self.__path = Path()

    def search(self, board):
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

                neighbor.h = self.__get_heuristic_value(neighbor, board.target_cell)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.previous = current_cell

                if neighbor not in self.__open_list:
                    self.__open_list.append(neighbor)

    def get_closed_list(self):
        return self.__closed_list

    def get_open_list(self):
        return self.__open_list

    def __get_heuristic_value(self, a: Cell, b: Cell):
        return math.hypot(a.x - b.x, a.y - b.y)

