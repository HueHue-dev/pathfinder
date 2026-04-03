from typing import List
from .node import Node


class Path:
    def __init__(self):
        self.__path: List[Node] = []

    def add(self, node: Node):
        self.__path.append(node)

    def get_path(self) -> List[Node]:
        return self.__path
