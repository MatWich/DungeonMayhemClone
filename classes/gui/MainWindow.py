from classes.game_logic.Data import Data
from classes.game_logic.Player import Player

try:
    from PyQt5.QtGui import QPainter, QPixmap
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
        self.data = Data.get_instance()
        #self.show_menu()
        self.starting_screen()
        #self.show_game_screen()


    def show_menu(self):
        self.setWindowTitle(TITLE)
        self.setMinimumWidth(850)
        self.setMinimumHeight(450)
        self.UIMenu = UIMenu(self)
        self.UIMenu.palladinBtn.clicked.connect(lambda: self.show_game_screen(self.UIMenu.palladinBtn))
        self.UIMenu.monkBtn.clicked.connect(lambda: self.show_game_screen(self.UIMenu.monkBtn))
        self.UIMenu.devilBtn.clicked.connect(lambda: self.show_game_screen(self.UIMenu.devilBtn))
        self.UIMenu.barbarianBtm.clicked.connect(lambda: self.show_game_screen(self.UIMenu.barbarianBtm))
        self.setCentralWidget(self.UIMenu)
        self.show()

    def show_game_screen(self, btn):
        self.data.player = Player(btn.text())
        self.data.enemy = Player(btn.text())
        self.setWindowTitle(TITLE)
        self.setMinimumWidth(850)
        self.setMinimumHeight(450)
        self.UIGame = UIGame(self)
        self.setCentralWidget(self.UIGame)
        self.show()

    def starting_screen(self):
        self.setWindowTitle(TITLE)
        self.setMinimumWidth(850)
        self.setMinimumHeight(450)
        self.UIStart = UIStart(self)
        self.setCentralWidget(self.UIStart)
        self.show()

    def paintEvent(self, event):  # set background_img
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap(os.path.join(ASSETS_DIR, "bg1.jpg"))  # Change to the relative path of your own image

        painter.drawPixmap(self.rect(), pixmap)
