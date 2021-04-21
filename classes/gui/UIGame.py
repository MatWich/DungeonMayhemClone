try:
    from classes.game_logic.Data import Data
    from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout, QHBoxLayout, QVBoxLayout
    from PyQt5.QtGui import QCursor, QPixmap, QFont
    from PyQt5 import QtCore
    from config import *
except ImportError:
    raise ImportError("Cannot import all modules")

class UIGame(QWidget):
    def __init__(self, parent):
        super(UIGame, self).__init__(parent)
        self.data = Data.get_instance()
        self.playerColor = None
        self.enemyColor = None

        self.initUI()


    def initUI(self):
        helthFont = QFont("Windlass", 15)
        actionsFont = QFont("Windlass", 15)
        shieldFont = QFont("Windlass", 15)
        nameFont = QFont("Windlass", 40)

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
        self.enemyNameLabel = QLabel(self.data.enemy.name)
        self.enemyNameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.enemyNameLabel.setStyleSheet("color: " + self.what_color(self.data.enemy) + ";")
        self.enemyNameLabel.setFont(nameFont)

        self.enemyHealth = QLabel()
        self.enemyHealth.setPixmap(QPixmap(os.path.join(ASSETS_DIR, "health.png")))
        self.enemyHealthCounter = QLabel(str(self.data.enemy.hp))
        self.enemyHealthCounter.setStyleSheet("color: rgb(214, 48, 2);")
        self.enemyHealthCounter.setFont(helthFont)

        self.enemyHealthBox = QHBoxLayout()
        self.enemyThunder = QLabel()
        self.enemyThunder.setPixmap(QPixmap(os.path.join(ASSETS_DIR, "thunder.png")))
        self.enemyThunderCounter = QLabel(str(self.data.enemy.actions))
        self.enemyThunderCounter.setStyleSheet("color: rgb(204, 180, 75);")
        self.enemyThunderCounter.setFont(actionsFont)

        self.enemyShield = QLabel()
        self.enemyShield.setPixmap(QPixmap(os.path.join(ASSETS_DIR, "shield.png")))
        self.enemyShieldCounter = QLabel(str(self.data.enemy.shield))
        self.enemyShieldCounter.setStyleSheet("color: rgb(153, 108, 12);")
        self.enemyShieldCounter.setFont(shieldFont)

        self.enemyHealthBox.addWidget(self.enemyHealth)
        self.enemyHealthBox.addWidget(self.enemyHealthCounter)
        self.enemyHealthBox.addWidget(self.enemyThunder)
        self.enemyHealthBox.addWidget(self.enemyThunderCounter)
        self.enemyHealthBox.addWidget(self.enemyShield)
        self.enemyHealthBox.addWidget(self.enemyShieldCounter)

        self.enemyCard = QLabel()
        self.enemyCard.setPixmap(QPixmap(os.path.join(ASSETS_DIR, "card.png")).scaled(200, 250))
        self.enemyInfo = QLabel("Enemy has his own tactic to choose cards :)")
        self.enemyInfo.setWordWrap(True)
        self.enemyInfo.setStyleSheet("""
        margin: 7px;
        padding: 6px;
        border: 1px solid red;
        border-radius: 4px;""" + "color: " + self.what_color(self.data.enemy))

        # PLAYER
        self.playerNameLabel = QLabel(self.data.player.name)
        self.playerNameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.playerNameLabel.setStyleSheet("color: " + self.what_color(self.data.player) + ";")
        self.playerNameLabel.setFont(nameFont)

        self.playerHealth = QLabel()
        self.playerHealth.setPixmap(QPixmap(os.path.join(ASSETS_DIR, "health.png")))
        self.playerHealthCounter = QLabel(str(self.data.player.hp))
        self.playerHealthCounter.setStyleSheet("color: rgb(214, 48, 2);" +
                                               "font-size: 14;")
        self.playerHealthCounter.setFont(helthFont)

        self.playerHealthBox = QHBoxLayout()
        self.playerThunder = QLabel()
        self.playerThunder.setPixmap(QPixmap(os.path.join(ASSETS_DIR, "thunder.png")))
        self.playerThunderCounter = QLabel(str(self.data.player.actions))
        self.playerThunderCounter.setFont(actionsFont)
        self.playerThunderCounter.setStyleSheet("color: rgb(204, 180, 75);")
        self.playerShield = QLabel()
        self.playerShield.setPixmap(QPixmap(os.path.join(ASSETS_DIR, "shield.png")))
        self.playerShieldCounter = QLabel(str(self.data.player.shield))
        self.playerShieldCounter.setStyleSheet("color: rgb(153, 108, 12);")
        self.playerShieldCounter.setFont(shieldFont)

        self.playerHealthBox.addWidget(self.playerHealth)
        self.playerHealthBox.addWidget(self.playerHealthCounter)
        self.playerHealthBox.addWidget(self.playerThunder)
        self.playerHealthBox.addWidget(self.playerThunderCounter)
        self.playerHealthBox.addWidget(self.playerShield)
        self.playerHealthBox.addWidget(self.playerShieldCounter)

        self.playerCard = QLabel()
        self.playerCard.setPixmap(QPixmap(os.path.join(ASSETS_DIR, "card.png")).scaled(200, 250))

        self.HboxLayout = QHBoxLayout()
        self.leftNavBtn = QPushButton("<")
        self.leftNavBtn.setStyleSheet(
                "*{ margin: 6px;" +
                "padding: 5px;" +
                "border: 1px solid" + self.what_color(self.data.player) + ";" +
                "border-radius: 3px;" +
                "color: " + self.what_color(self.data.player) + "; }" +
                "*:hover {" +
                "background: " + self.what_color(self.data.player) + ";" +
                "color: white;" +
                "}"
                )

        self.rightNavBtn = QPushButton(">")
        self.rightNavBtn.setStyleSheet(
                "*{ margin: 6px;" +
                "padding: 5px;" +
                "border: 1px solid" + self.what_color(self.data.player) + ";" +
                "border-radius: 3px;" +
                "color: " + self.what_color(self.data.player) + "; }" +
                "*:hover {" +
                "background: " + self.what_color(self.data.player) + ";" +
                "color: white;" +
                "}"
                )

        self.pickBtn = QPushButton("Play")
        self.pickBtn.setStyleSheet(
                "*{ margin: 6px;" +
                "padding: 5px;" +
                "border: 1px solid" + self.what_color(self.data.player) + ";" +
                "border-radius: 3px;" +
                "color: " + self.what_color(self.data.player) + "; }" +
                "*:hover {" +
                "background: " + self.what_color(self.data.player) + ";" +
                "color: white;" +
                "}"
                )

        self.HboxLayout.addWidget(self.leftNavBtn)
        self.HboxLayout.addWidget(self.pickBtn)
        self.HboxLayout.addWidget(self.rightNavBtn)

        self.enemyWBoxLayout = QVBoxLayout()
        self.enemyWBoxLayout.addWidget(self.enemyNameLabel)
        self.enemyWBoxLayout.addLayout(self.enemyHealthBox)

        self.playerVBoxLayout = QVBoxLayout()
        self.playerVBoxLayout.addWidget(self.playerNameLabel)
        self.playerVBoxLayout.addLayout(self.playerHealthBox)


        # ROW 0
        self.layout.addLayout(self.enemyWBoxLayout, 0, 0, 1, 1)
        self.layout.addWidget(self.mainLabel, 0, 1, 1, 1)
        self.layout.addLayout(self.playerVBoxLayout, 0, 2, 1, 1)
        # ROW 1
        self.layout.addWidget(self.enemyCard, 1, 0, 1, 1)
        self.layout.addWidget(self.playerCard, 1, 2, 1, 1)
        # ROW 2
        self.layout.addWidget(self.enemyInfo, 2, 0, 1, 1)
        self.layout.addLayout(self.HboxLayout, 2, 2, 1, 1)

        self.setLayout(self.layout)

    def rightNavBtnOnclick(self):
        pass

    def leftNavBtnOnclick(self):
        pass

    def what_color(self, player):
        if player.color == RED:
            return "#CC3300"
        elif player.color == YELLOW:
            return "#CCCC66"
        elif player.color == PURPLE:
            return "#9933CC"
        elif player.color == GREEN:
            return "#66CC66"
        else:
            raise Exception("Something went wrong with player color")
