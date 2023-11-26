import math
from .cell import Cell


class AStar:
    def __init__(self):
        self.open_list = []
        self.closed_list = []
        self.path = []

    def search(self, board):
        self.open_list.append(board.start_cell)
        while len(self.open_list) > 0:
            lowest_index = 0
            for i, cell in enumerate(self.open_list):
                if cell.f < self.open_list[lowest_index].f:
                    lowest_index = i

            current_cell = self.open_list[lowest_index]

            if current_cell.is_target:
                temp = current_cell
                while isinstance(temp.previous, Cell):
                    self.path.append(temp.previous)
                    temp = temp.previous
                return self.path

            self.open_list.remove(current_cell)
            self.closed_list.append(current_cell)

            for neighbor in current_cell.neighbors:
                if neighbor in self.closed_list:
                    continue

                neighbor.g = current_cell.g + 1

                neighbor.h = self.get_heuristic_value(neighbor, board.target_cell)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.previous = current_cell

                if neighbor not in self.open_list:
                    self.open_list.append(neighbor)

    def get_heuristic_value(self, cell1, cell2):
        return math.hypot(cell1.x - cell2.x, cell1.y - cell2.y)
