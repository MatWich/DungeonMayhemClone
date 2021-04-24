try:
    import random
    from PyQt5.QtGui import QPainter, QPixmap
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
    from classes.gui.UIMenu import UIMenu
    from classes.gui.UIStart import UIStart
    from classes.gui.UIGame import UIGame
    from config import *
    from classes.game_logic.Data import Data
    from classes.game_logic.Player import Player
except ImportError:

    raise ImportError("Cannot import all modules")


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.started = False
        self.data = Data.get_instance()
        #self.show_menu()
        self.starting_screen()
        #self.show_game_screen()

    def show_menu(self):
        self.setWindowTitle(TITLE)
        self.setMinimumWidth(SCR_SIZE[0])
        self.setMinimumHeight(SCR_SIZE[1])
        self.UIMenu = UIMenu(self)
        self.UIMenu.palladinBtn.clicked.connect(lambda: self.show_game_screen(self.UIMenu.palladinBtn))
        self.UIMenu.monkBtn.clicked.connect(lambda: self.show_game_screen(self.UIMenu.monkBtn))
        self.UIMenu.devilBtn.clicked.connect(lambda: self.show_game_screen(self.UIMenu.devilBtn))
        self.UIMenu.barbarianBtm.clicked.connect(lambda: self.show_game_screen(self.UIMenu.barbarianBtm))
        self.setCentralWidget(self.UIMenu)
        self.show()

    def show_game_screen(self, btn=None):
        if not self.data.started:
            decks_available = [RED, YELLOW, PURPLE, GREEN]
            decks_available.remove(btn.text())
            index = random.randint(0, len(decks_available) - 1)
            self.data.player = Player(btn.text(), "Player")
            self.data.enemy = Player(decks_available[index], "Enemy")
            self.data.started = True
        self.setWindowTitle(TITLE)
        self.setMinimumWidth(SCR_SIZE[0])
        self.setMinimumHeight(SCR_SIZE[1])
        self.UIGame = UIGame(self)
        self.setCentralWidget(self.UIGame)
        self.show()

    def starting_screen(self):
        self.setWindowTitle(TITLE)
        self.setMinimumWidth(SCR_SIZE[0])
        self.setMinimumHeight(SCR_SIZE[1])
        self.UIStart = UIStart(self)
        self.setCentralWidget(self.UIStart)
        self.show()

    def paintEvent(self, event):  # set background_img
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap(os.path.join(ASSETS_DIR, "bg1.jpg"))  # Change to the relative path of your own image

        painter.drawPixmap(self.rect(), pixmap)
