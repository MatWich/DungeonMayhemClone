try:
    import os
except ImportError:
    raise ImportError("Cannot import all modules")


PROJECT_DIR = os.path.dirname(__file__)
ASSETS_DIR = os.path.join(PROJECT_DIR, "assets")

