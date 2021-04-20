try:
    from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout
    from PyQt5.QtGui import QCursor, QPixmap, QMouseEvent
    from PyQt5 import QtCore, QtGui
    from config import *
except ImportError:
    raise ImportError("Cannot import all modules")


class UIMenu(QWidget):
    def __init__(self, parent=None):
        super(UIMenu, self).__init__(parent)
        self.layout = QGridLayout()
        keys = []
        self.parent = parent
        # beacuse keys() returns not indexable object
        for key in COLOR_LIST.keys():
            keys.append(key)

        self.setStyleSheet("*{ margin: 0px;"
                           "padding: 0px;"
                           "font-family: windlass;}")
        self.label = QLabel()
        self.label.setText("Choose your deck")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("""QWidget{
            font-size: 52px;
            margin: 10px;
            width: 50%;
        }""")

        # buttons
        self.palladinBtn = self.create_button(keys[0])
        self.monkBtn = self.create_button(keys[1])
        self.devilBtn = self.create_button(keys[2])
        self.barbarianBtm = self.create_button(keys[3])

        self.layout.addWidget(self.label, 0, 0, 1, 2)
        self.layout.addWidget(self.palladinBtn, 1, 0)
        self.layout.addWidget(self.monkBtn, 1, 1)
        self.layout.addWidget(self.devilBtn, 2, 0)
        self.layout.addWidget(self.barbarianBtm, 2, 1)
        self.setLayout(self.layout)

    """ HELPERS """
    def create_button(self, text):
        button = QPushButton(text)
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.setStyleSheet("*{border: 3px solid " + COLOR_LIST[text] + ";" +
                             "color: " + COLOR_LIST[text] + ";" +
                             "margin: 10px;" +
                             "padding: 6px;" +
                             "border-radius: 5px;" +
                             "font-size: 20px;" +
                             "}" +
                             "*:hover{" +
                             "color: #fff;" +
                             "background: " + COLOR_LIST[text] + ";" +
                             "}"
                             )
        return button
