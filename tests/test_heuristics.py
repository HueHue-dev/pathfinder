import pytest
from core.node import Node
from core.heuristics.manhattan import Manhattan
from core.heuristics.euclidean import Euclidean
from core.heuristics.diagonal import Diagonal

def test_manhattan_distance():
    m = Manhattan()
    node_a = Node(0, 0, 10) # x=0, y=0
    node_b = Node(2, 3, 10) # x=20, y=30
    
    # Manhattan: |0-20| + |0-30| = 50
    assert m.get_distance(node_a, node_b) == 50
    assert not m.is_diagonal()

def test_euclidean_distance():
    e = Euclidean()
    node_a = Node(0, 0, 10)
    node_b = Node(3, 4, 10) # x=30, y=40
    
    # Euclidean: sqrt(30^2 + 40^2) = 50
    assert e.get_distance(node_a, node_b) == 50
    assert e.is_diagonal()

def test_diagonal_distance():
    d = Diagonal()
    node_a = Node(0, 0, 10)
    node_b = Node(1, 1, 10) # x=10, y=10

    assert d.is_diagonal()
    assert d.get_distance(node_a, node_b) >= 0
