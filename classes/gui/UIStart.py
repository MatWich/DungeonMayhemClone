try:
    from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout, QGraphicsOpacityEffect
    from PyQt5.QtGui import QCursor, QPixmap, QMouseEvent
    from PyQt5 import QtCore, QtGui, Qt
    import os
    from config import *
    from time import process_time_ns, sleep, time
    import threading
    from PyQt5.QtCore import QTimer, QThreadPool
    from PyQt5.Qt import Qt
except ImportError:
    raise ImportError("Cannot import all modules")

""" After you start the app you should be able to press any button to change the window to the menu one"""


class UIStart(QWidget):
    def __init__(self, parent=None):
        super(UIStart, self).__init__(parent=parent)
        self.layout = QGridLayout()
        self.label = QLabel()
        self.timer = QTimer()
        self.counter = 0
        self.threadpool = QThreadPool()
        #self.parent = parent

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

        self.textLabel = QLabel("Click anywhere to start")
        self.textLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.label, 0, 0, 1, 2)
        self.layout.addWidget(self.textLabel, 1, 0, 1, 2)
        self.setLayout(self.layout)
        self.fading()

        self.timer.setInterval(1001)    # you have to pass here bigger time than animationtime
        self.timer.timeout.connect(lambda: self.fade(self.textLabel))
        self.timer.start()

    def fading(self):
        self.counter += 1
        if self.counter % 2 == 0:
            self.fade(self.textLabel)
        else:
            if self.counter == 3:
                self.counter = -1
            self.unfade(self.textLabel)

    def fade(self, widget):
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()

    def unfade(self, widget):
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    # def mousePressEvent(self, event):
    #     #print(QMouseEvent.pos())
    #     #self.parent.show_menu()
    #     if event.key() == Qt.Key_Space:
    #         self.parent.parent().parent().

    def mousePressEvent(self, QMouseEvent):
        print(QMouseEvent.pos())
        self.timer.killTimer(self.timer.timerId())

        # it actuall works XDD
        x = lambda : self.parent().show_menu()
        x()