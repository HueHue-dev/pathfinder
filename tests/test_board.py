import pytest
import os

# Set SDL_VIDEODRIVER to dummy to avoid opening a window
os.environ['SDL_VIDEODRIVER'] = 'dummy'
import pygame as pg

# Initialize pygame for font system (required by Board)
pg.init()
pg.font.init()

from core.board import Board

def test_board_initialization():
    rows = 10
    board = Board(rows)
    assert len(board.grid) == rows
    assert len(board.grid[0]) == rows
    assert board.start_node is None
    assert board.target_node is None

def test_board_get_pos():
    rows = 20 # Config.BOARD_WIDTH is 600, so gap is 30
    board = Board(rows)
    
    row, col = board.get_pos((65, 95)) # x=65, y=95
    # gap = 800 // 20 = 40
    # row = 65 // 40 = 1
    # col = 95 // 40 = 2
    assert row == 1
    assert col == 2

def test_set_neighbours_no_diagonal():
    board = Board(3)
    board.set_neighbours(with_diagonal=False)
    center_node = board.grid[1][1]
    assert len(center_node.neighbors) == 4
    
    top_left = board.grid[0][0]
    assert len(top_left.neighbors) == 2 # Right and Down

def test_set_neighbours_with_diagonal():
    board = Board(3)
    board.set_neighbours(with_diagonal=True)
    center_node = board.grid[1][1]
    assert len(center_node.neighbors) == 8
    
    top_left = board.grid[0][0]
    assert len(top_left.neighbors) == 3 # Right, Down, Down-Right

def test_barrier_affects_neighbors():
    board = Board(3)
    board.grid[1][2].set_barrier()
    board.set_neighbours(with_diagonal=False)
    
    center_node = board.grid[1][1]
    assert len(center_node.neighbors) == 3
    assert board.grid[1][2] not in center_node.neighbors
