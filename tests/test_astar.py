import pytest
import os

# Set SDL_VIDEODRIVER to dummy to avoid opening a window
os.environ['SDL_VIDEODRIVER'] = 'dummy'
import pygame as pg

# Initialize pygame for font system (required by Board)
pg.init()
pg.font.init()

from core.board import Board
from core.astar import AStar
from core.node import Node

def test_astar_simple_path():
    board = Board(10)
    astar = AStar()
    
    start = board.grid[0][0]
    target = board.grid[0][2]
    
    start.set_start()
    target.set_target()
    board.start_node = start
    board.target_node = target
    
    board.set_neighbours(with_diagonal=False)
    path = astar.search(board)
    
    assert path is not None
    # Path from (0,0) to (0,2) should be (0,1) and (0,0)
    nodes = path.get_path()
    assert len(nodes) == 2
    assert nodes[0] == board.grid[0][1]
    assert nodes[1] == board.grid[0][0]

def test_astar_no_path():
    board = Board(5)
    astar = AStar()
    
    start = board.grid[0][0]
    target = board.grid[4][4]
    
    start.set_start()
    target.set_target()
    board.start_node = start
    board.target_node = target
    
    # Create a wall
    for i in range(5):
        board.grid[i][2].set_barrier()
    
    board.set_neighbours(with_diagonal=False)
    path = astar.search(board)
    
    assert path is None

def test_astar_diagonal_path():
    board = Board(5)
    astar = AStar()
    
    start = board.grid[0][0]
    target = board.grid[1][1]
    
    start.set_start()
    target.set_target()
    board.start_node = start
    board.target_node = target
    
    # Test with diagonal allowed
    astar.set_heuristic("Diagonal")
    
    board.set_neighbours(with_diagonal=True)
    path = astar.search(board)
    
    assert path is not None
    # With diagonal, (0,0) to (1,1) is 1 step (adds (0,0) to path)
    assert len(path.get_path()) == 1
    assert path.get_path()[0] == board.grid[0][0]
