from .node import Node


class Path:
    def __init__(self):
        self.__path = []

    def add(self, node: Node):
        self.__path.append(node)

    def get_path(self):
        return self.__path
