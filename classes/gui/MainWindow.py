try:
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
    from classes.gui.UIMenu import UIMenu
    from classes.gui.UIStart import UIStart
    from classes.gui.UIGame import UIGame
    from config import *
except ImportError:

    raise ImportError("Cannot import all modules")


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        #self.show_menu()
        self.starting_screen()
        #self.show_game_screen()


    def show_menu(self):
        self.setWindowTitle(TITLE)
        self.setMinimumWidth(800)
        self.setMinimumHeight(450)
        self.UIMenu = UIMenu(self)
        self.UIMenu.palladinBtn.clicked.connect(lambda: self.show_game_screen())
        self.UIMenu.monkBtn.clicked.connect(lambda: self.show_game_screen())
        self.UIMenu.devilBtn.clicked.connect(lambda: self.show_game_screen())
        self.UIMenu.barbarianBtm.clicked.connect(lambda: self.show_game_screen())
        self.setCentralWidget(self.UIMenu)
        self.show()

    def show_game_screen(self):
        self.setWindowTitle(TITLE)
        self.setMinimumWidth(800)
        self.setMinimumHeight(450)
        self.UIGame = UIGame(self)
        self.setCentralWidget(self.UIGame)
        self.show()

    def starting_screen(self):
        self.setWindowTitle(TITLE)
        self.setMinimumWidth(800)
        self.setMinimumHeight(450)
        self.UIStart = UIStart(self)
        self.setCentralWidget(self.UIStart)
        self.show()
