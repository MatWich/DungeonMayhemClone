from PyQt5.QtCore import QVariantAnimation, QVariant, pyqtSlot, QEasingCurve, QEventLoop, QTimer
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QLabel


class AnimationLabel(QLabel):
    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)
        self.animation = QVariantAnimation()
        self.animation.valueChanged.connect(self.changeColor)

    @pyqtSlot(QVariant)
    def changeColor(self, color):
        palette = self.palette()
        palette.setColor(QPalette.WindowText, color)
        self.setPalette(palette)

    def startFadeIn(self):
        self.animation.stop()
        self.animation.setStartValue(QColor(0, 0, 0, 0))
        self.animation.setEndValue(QColor(0, 0, 0, 255))
        self.animation.setDuration(2000)
        self.animation.setEasingCurve(QEasingCurve.InBack)
        self.animation.start()
        if self.animation.endValue() == QColor(0,0,0,255):
            QTimer.singleShot(2000, self.startFadeOut)

    def startFadeOut(self):
        self.animation.stop()
        self.animation.setStartValue(QColor(0, 0, 0, 255))
        self.animation.setEndValue(QColor(0, 0, 0, 0))
        self.animation.setDuration(2000)
        self.animation.setEasingCurve(QEasingCurve.OutBack)
        self.animation.start()
        if self.animation.endValue() == QColor(0,0,0,0):
            QTimer.singleShot(2000, self.startFadeIn)

    def startAnimation(self):
        self.startFadeIn()
        loop = QEventLoop()
        self.animation.finished.connect(loop.quit)
        loop.exec_()
        timer = QTimer()
        #timer.setSingleShot(False)
        timer.singleShot(2000, self.startFadeOut)
