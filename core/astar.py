import heapq
from .node import Node
from .path import Path
from .heuristicFactory import HeuristicFactory


class AStar:
    def __init__(self):
        self.__open_list = []
        self.__closed_list = set()
        self.__path = Path()
        self.__heuristic = HeuristicFactory().get_heuristic()

    def search(self, board) -> Path:
        count = 0
        heapq.heappush(self.__open_list, (0, count, board.start_node))
        open_set = {board.start_node}

        while self.__open_list:
            current_node = heapq.heappop(self.__open_list)[2]
            open_set.remove(current_node)

            if current_node.is_target:
                temp = current_node
                while isinstance(temp.previous, Node):
                    self.__path.add(temp.previous)
                    temp = temp.previous
                return self.__path

            self.__closed_list.add(current_node)

            for neighbor in current_node.neighbors:
                if neighbor in self.__closed_list:
                    continue

                temp_g = current_node.g + 1

                if neighbor not in open_set or temp_g < neighbor.g:
                    neighbor.previous = current_node
                    neighbor.g = temp_g
                    neighbor.h = self.__heuristic.get_distance(neighbor, board.target_node)
                    neighbor.f = neighbor.g + neighbor.h
                    if neighbor not in open_set:
                        count += 1
                        heapq.heappush(self.__open_list, (neighbor.f, count, neighbor))
                        open_set.add(neighbor)

    def get_closed_list(self):
        return list(self.__closed_list)

    def get_open_list(self):
        # We need to return the nodes from the heap for visualization
        return [item[2] for item in self.__open_list]

    def reset(self):
        self.__open_list = []
        self.__closed_list = set()
        self.__path = Path()

    def set_heuristic(self, heuristic: str):
        self.__heuristic = HeuristicFactory().get_heuristic(heuristic)

    def get_heuristic(self):
        return self.__heuristic
