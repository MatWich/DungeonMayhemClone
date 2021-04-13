try:
    from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout
    from PyQt5.QtGui import QCursor, QPixmap, QMouseEvent
    from PyQt5 import QtCore, QtGui
except ImportError:
    raise ImportError("Cannot import all modules")

colorList = {"Palladin": "rgb(214, 48, 2)",
             "Monk": "rgb(204, 180, 75)",
             "Devil": "rgb(170, 75, 204)",
             "Barbarian": "rgb(75, 204, 122)"
             }


class UIMenu(QWidget):
    def __init__(self, parent=None):
        super(UIMenu, self).__init__(parent)
        self.layout = QGridLayout()
        self.setStyleSheet("*{ margin: 0px;"
                           "padding: 0px;"
                           "font-family: windlass;}")
        self.label = QLabel()
        self.label.setText("Choose your deck")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.label.setStyleSheet("""QWidget{
            font-size: 52px;
            margin: 10px;
            width: 50%;
        }""")

        # buttons
        self.palladinBtn = self.create_button("Palladin")
        self.monkBtn = self.create_button("Monk")
        self.devilBtn = self.create_button("Devil")
        self.barbarianBtm = self.create_button("Barbarian")

        # button onclicks
        self.palladinBtn.clicked.connect(lambda: self.palladinBtnOnClick(self.palladinBtn))
        self.monkBtn.clicked.connect(lambda: self.monkBtnOnClick(self.monkBtn))
        self.devilBtn.clicked.connect(lambda: self.devilBtnOnClick(self.devilBtn))
        self.barbarianBtm.clicked.connect(lambda: self.barbarianBtnOnClick(self.barbarianBtm))

        self.layout.addWidget(self.label, 0, 0, 1, 2)
        self.layout.addWidget(self.palladinBtn, 1, 0)
        self.layout.addWidget(self.monkBtn, 1, 1)
        self.layout.addWidget(self.devilBtn, 2, 0)
        self.layout.addWidget(self.barbarianBtm, 2, 1)
        self.setLayout(self.layout)

    def create_button(self, text):
        button = QPushButton(text)
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.setStyleSheet("*{border: 3px solid " + colorList[text] + ";" +
                             "color: " + colorList[text] + ";" +
                             "margin: 10px;" +
                             "padding: 6px;" +
                             "border-radius: 5px;" +
                             "font-size: 20px;" +
                             "}" +
                             "*:hover{" +
                             "color: #fff;" +
                             "background: " + colorList[text] + ";" +
                             "}"
                             )
        return button

    """ ON CLICKS """
    def palladinBtnOnClick(self, b):
        print(f"{b.text()} button clicked")

    def devilBtnOnClick(self, b):
        print(f"{b.text()} button clicked")

    def monkBtnOnClick(self, b):
        print(f"{b.text()} button clicked")

    def barbarianBtnOnClick(self, b):
        print(f"{b.text()} button clicked")