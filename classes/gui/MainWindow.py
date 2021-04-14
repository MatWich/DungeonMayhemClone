try:
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
    from classes.gui.UIMenu import UIMenu
    from classes.gui.UIStart import UIStart
except ImportError:
    raise ImportError("Cannot import all modules")


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        #self.show_menu()
        self.starting_screen()

    def show_menu(self):
        self.setWindowTitle("Dungeon Maythem Clone Game")
        self.setMinimumWidth(800)
        self.setMinimumHeight(450)
        self.UIMenu = UIMenu()
        self.setCentralWidget(self.UIMenu)
        self.show()

    def show_game_screen(self):
        self.setWindowTitle("Dungeon Maythem Clone Game")
        self.setMinimumWidth(800)
        self.setMinimumHeight(450)
        self.show()

    def starting_screen(self):
        self.setWindowTitle("Dungeon Maythem Clone Game")
        self.setMinimumWidth(800)
        self.setMinimumHeight(450)
        self.UIStart = UIStart(self)
        self.setCentralWidget(self.UIStart)
        self.show()
