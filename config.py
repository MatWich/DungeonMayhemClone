try:
    import os
except ImportError:
    raise ImportError("Cannot import all modules in config.py")

TITLE = "Dungeon Maythem Clone Game"

PROJECT_DIR = os.path.dirname(__file__)
ASSETS_DIR = os.path.join(PROJECT_DIR, "assets")

COLOR_LIST = {"Palladin": "rgb(214, 48, 2)",
             "Monk": "rgb(204, 180, 75)",
             "Devil": "rgb(170, 75, 204)",
             "Barbarian": "rgb(75, 204, 122)"
              }
