class Config:
    APP_TITLE = "Pathfinding Visualizer"
    WIDTH = 800
    HEIGHT = 960
    BOARD_WIDTH = WIDTH
    ROWS = 10
    GAP = BOARD_WIDTH // ROWS
    
    # Colors
    COLOR_DEFAULT = (0, 0, 0)
    COLOR_START = (0, 128, 34)
    COLOR_TARGET = (155, 0, 0)
    COLOR_BARRIER = (255, 255, 255)
    COLOR_PATH = (0, 89, 255)
    COLOR_CLOSED = (100, 100, 100)
    COLOR_OPEN = (152, 179, 0)
    COLOR_GRID = (255, 255, 255)
    COLOR_TEXT = (255, 255, 255)
