try:
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
except ImportError:
    raise ImportError("Cannot import all modules")


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.show_menu()

    def show_menu(self):
        self.setWindowTitle("Dungeon Maythem Clone Game")
        self.setMinimumWidth(800)
        self.setMinimumHeight(450)
        self.show()

    def show_game_screen(self):
        self.setWindowTitle("Dungeon Maythem Clone Game")
        self.setMinimumWidth(800)
        self.setMinimumHeight(450)
        self.show()
