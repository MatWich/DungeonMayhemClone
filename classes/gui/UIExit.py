try:
    from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout, QApplication
    from PyQt5.QtGui import QCursor, QPixmap, QMouseEvent, QFont
    from PyQt5 import QtCore, QtGui
    from config import *
except ImportError:
    raise ImportError("Cannot import all modules")


class UIExit(QWidget):
    def __init__(self, parent=None):
        super(UIExit, self).__init__(parent)
        self.layout = QGridLayout()
        self.parent = parent
        font = QFont("Windlass", 40)
        self.label = QLabel()
        self.label.setText("Thanks for playing")
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.layout.addWidget(self.label, 0, 0)
        self.setLayout(self.layout)

    def mousePressEvent(self, QMouseEvent):
        print(QMouseEvent.pos())
        exit()

