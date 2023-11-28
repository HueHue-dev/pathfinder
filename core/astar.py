import numpy as np
from .node import Node
from .path import Path
from .heuristicFactory import HeuristicFactory


class AStar:
    def __init__(self):
        self.__open_list = []
        self.__closed_list = []
        self.__path = Path()
        self.__heuristic = HeuristicFactory().get_heuristic()

    def search(self, board) -> Path:
        self.__open_list.append(board.start_node)
        while len(self.__open_list) > 0:
            lowest_index = 0
            for i, node in enumerate(self.__open_list):
                if node.f < self.__open_list[lowest_index].f:
                    lowest_index = i

            current_node = self.__open_list[lowest_index]

            if current_node.is_target:
                temp = current_node
                while isinstance(temp.previous, Node):
                    self.__path.add(temp.previous)
                    temp = temp.previous
                return self.__path

            self.__open_list.remove(current_node)
            self.__closed_list.append(current_node)

            for neighbor in current_node.neighbors:
                if neighbor in self.__closed_list:
                    continue

                neighbor.g = current_node.g + 1

                neighbor.h = self.__heuristic.get_distance(neighbor, board.target_node)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.previous = current_node

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

    def set_heuristic(self, heuristic: str):
        self.__heuristic = HeuristicFactory().get_heuristic(heuristic)

    def get_heuristic(self):
        return self.__heuristic
