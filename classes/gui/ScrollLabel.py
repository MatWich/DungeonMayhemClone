try:
    from PyQt5.QtWidgets import *
    from PyQt5 import QtCore, QtGui
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    import sys
except ImportError:
    raise ImportError("Cannot import all modules in ScrollLabel.py")


class ScrollLabel(QScrollArea):
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)
        self.setWidgetResizable(True)
        # making qwidget object
        content = QWidget(self)
        self.setWidget(content)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet("""background-color: rgba(0,0,0,0);""")
        layout = QVBoxLayout(content)
        self.label = QLabel(content)
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.label.setWordWrap(True)
        layout.addWidget(self.label)


    def setText(self, text):
        self.label.setText(text)

# class ScrollLabel(QScrollArea):
#     def __init__(self, *args, **kwargs):
#         QScrollArea.__init__(self, *args, **kwargs)
#         # #self.verticalScrollBar().setEnabled(True)
#         # self.setWidgetResizable(True)
#         # # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
#         # # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
#         # content = QWidget(self)
#         # self.setWidget(content)
#         # layout = QVBoxLayout()
#         # self.label = QLabel(content)
#         # self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
#         # self.label.setWordWrap(True)
#         # layout.addWidget(self.label)
#         # self.setWidgetResizable(True)
#         # making qwidget object
#
#         content = QWidget(self)
#
#         self.setWidget(content)
#
#         layout = QVBoxLayout(content)
#
#         self.label = QLabel(content)
#
#         self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
#
#         self.label.setWordWrap(True)
#
#         layout.addWidget(self.label)
#
#     def setText(self, text):
#         self.label.setText(text)
