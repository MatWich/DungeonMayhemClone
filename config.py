try:
    import os
except ImportError:
    raise ImportError("Cannot import all modules in config.py")

SCR_SIZE = (WIDTH, HEIGHT) = (900, 500)
TITLE = "Dungeon Maythem Clone Game"

PROJECT_DIR = os.path.dirname(__file__)
ASSETS_DIR = os.path.join(PROJECT_DIR, "assets")
RED_DECK_DIR = os.path.join(ASSETS_DIR, "red_deck")

RED = "Palladin"
YELLOW = "Monk"
PURPLE = "Devil"
GREEN = "Barbarian"

COLOR_LIST = {RED: "rgb(214, 48, 2)",
              YELLOW: "rgb(204, 180, 75)",
              PURPLE: "rgb(170, 75, 204)",
              GREEN: "rgb(75, 204, 122)"
              }
