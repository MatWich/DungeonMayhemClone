from PyQt5.QtCore import QTimer

try:
    from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout, QGraphicsOpacityEffect
    from PyQt5.QtGui import QCursor, QPixmap, QMouseEvent
    from PyQt5 import QtCore, QtGui
    from classes.gui.AnimationLabel import AnimationLabel
    import os
    from config import *
    from time import process_time_ns
    import threading
except ImportError:
    raise ImportError("Cannot import all modules")

""" After you start the app you should be able to press any button to change the window to the menu one"""


class UIStart(QWidget):
    def __init__(self, parent=None):
        super(UIStart, self).__init__(parent)
        self.layout = QGridLayout()
        self.label = QLabel()

        image = QPixmap(os.path.join(ASSETS_DIR, "Dungeon-Mayhem-logo1.png"))
        self.label.setPixmap(image)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label.setStyleSheet("*{"
                                 "margin: 0;"
                                 "padding: 0;"
                                 "width: 50%;"
                                 "height: 100%;"
                                 "background-position: center;"
                                 "background-repeat: no-repeat;"
                                 "background-size: cover;"
                                 "}")


        self.textLabel = AnimationLabel("Click anywhere to start")
        self.textLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.textLabel.startAnimation()

        self.layout.addWidget(self.label, 0, 0, 1, 2)
        self.layout.addWidget(self.textLabel, 1, 0, 1, 2)
        self.setLayout(self.layout)


    # def fade(self, widget):
    #     widget.setWindowOpacity(0.5)
    #     QTimer.singleShot(1000, self.unfade)
    #
    # def unfade(self, widget):
    #     widget.setWindowOpacity(1)
    #     QTimer.singleShot(1000, self.fade)
    #
    #

