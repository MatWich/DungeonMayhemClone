try:
    from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout, QHBoxLayout
    from PyQt5.QtGui import QCursor, QPixmap
    from PyQt5 import QtCore
    from config import *
except ImportError:
    raise ImportError("Cannot import all modules")

class UIGame(QWidget):
    def __init__(self, parent):
        super(UIGame, self).__init__(parent)

        self.setStyleSheet("""
                *{
                    margin: 0px;
                    padding: 0px;
                    font-family: windlass;
                }
                """)
        self.layout = QGridLayout()
        self.mainLabel = QLabel("BATTLE")
        self.mainLabel.setScaledContents(True)

        self.mainLabel.setStyleSheet("""
                    *{
                        margin: 10px;
                        padding: 1px;
                        font-size: 74px;
                        background-position: center;
                        background-repeat: no-repeat;
                        background-size: cover;
                    }
                    """)
        self.mainLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        # ENEMY
        self.enemyLabel = QLabel("Enemy")
        self.enemyLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.enemyCard = QLabel()
        self.enemyCard.setPixmap(QPixmap(os.path.join(ASSETS_DIR, "card.png")).scaled(200, 250))
        self.enemyInfo = QLabel("Enemy has his own tactic to choose cards :)")
        self.enemyInfo.setWordWrap(True)
        self.enemyInfo.setStyleSheet("""
        margin: 7px;
        padding: 6px;
        border: 1px solid red;
        border-radius: 4px;""")
        # PLAYER
        self.playerLabel = QLabel("Player")
        self.playerLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.playerCard = QLabel("vnsdivn")
        self.playerCard.setPixmap(QPixmap(os.path.join(ASSETS_DIR, "card.png")).scaled(200, 250))
        self.HboxLayout = QHBoxLayout()
        self.leftNavBtn = QPushButton(">")
        self.leftNavBtn.setStyleSheet("""
        margin: 7px;
        padding: 6px;
        border: 1px solid red;
        border-radius: 4px;
        """)
        self.rightNavBtn = QPushButton("<")
        self.rightNavBtn.setStyleSheet("""
        margin: 7px;
        padding: 6px;
        border: 1px solid red;
        border-radius: 4px;
        """)
        self.HboxLayout.addWidget(self.leftNavBtn)
        self.HboxLayout.addWidget(self.rightNavBtn)

        # ROW 0
        self.layout.addWidget(self.enemyLabel, 0, 0, 1, 1)
        self.layout.addWidget(self.mainLabel, 0, 1, 1, 1)
        self.layout.addWidget(self.playerLabel, 0, 2, 1, 1)
        # ROW 1
        self.layout.addWidget(self.enemyCard, 1, 0, 1, 1)
        self.layout.addWidget(self.playerCard, 1, 2, 1, 1)
        # ROW 2
        self.layout.addWidget(self.enemyInfo, 2, 0, 1, 1)
        self.layout.addLayout(self.HboxLayout, 2, 2, 1, 1 )

        self.setLayout(self.layout)

    def rightNavBtnOnclick(self):
        pass

    def leftNavBtnOnclick(self):
        pass