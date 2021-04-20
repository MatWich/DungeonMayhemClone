try:
    from classes.game_logic.Card import Card
    from config import *
except ImportError:

    raise ImportError("Cannot import all modules")


class Data:
    _instance = None
    @staticmethod
    def get_instance():
        if Data._instance == None:
            Data()
        return Data._instance

    def __init__(self):
        if Data._instance != None:
            raise Exception("To je singleton tego nie wywolasz 2 razy :)")
        else:
            Data._instance = self
        self.player = None
        self.enemy = None
        self.redDeck = []
        self.yellowDeck = []
        self.purpleDeck = []
        self.greenDeck = []
        self.set_up()



    def set_up(self):
        self.set_up_redDeck()

    def set_up_redDeck(self):
        # 3
        c0 = {"name": "For Juistice!",
              "attack": 1,
              "actions": 1,
              "draw": 0,
              "heal": 0,
              "shield": 0}
        # 2
        c1 = {"name": "For The Most Juistice!",
              "attack": 3,
              "actions": 0,
              "draw": 0,
              "heal": 0,
              "shield": 0}
        # 2
        c2 = {"name": "Finger-wag of Judgment",
              "attack": 0,
              "actions": 2,
              "draw": 0,
              "heal": 0,
              "shield": 0}
        # 2
        c3 = {"name": "Spinning Parry",
              "attack": 0,
              "actions": 0,
              "draw": 1,
              "heal": 0,
              "shield": 1}
        # 3
        c4 = {"name": "Fighting Words",
              "attack": 2,
              "actions": 0,
              "draw": 0,
              "heal": 1,
              "shield": 0}
        # 3
        c5 = {"name": "Divine Smite",
              "attack": 3,
              "actions": 0,
              "draw": 0,
              "heal": 1,
              "shield": 0}
        # 2
        c6 = {"name": "High Charisma",
              "attack": 0,
              "actions": 0,
              "draw": 2,
              "heal": 0,
              "shield": 0}
        # 4
        c7 = {"name": "For Even More Juistice!",
              "attack": 2,
              "actions": 0,
              "draw": 0,
              "heal": 0,
              "shield": 0}
        # 2
        c8 = {"name": "Divine Shield",
              "attack": 0,
              "actions": 0,
              "draw": 0,
              "heal": 0,
              "shield": 3}
        # 1
        c9 = {"name": "Fluffy",
              "attack": 0,
              "actions": 0,
              "draw": 0,
              "heal": 0,
              "shield": 2}
        # 1
        c10 = {"name": "Cure Wounds",
               "attack": 0,
               "actions": 0,
               "draw": 2,
               "heal": 1,
               "shield": 0}

        self.redDeck.append(Card(c0))
        self.redDeck.append(Card(c0))
        self.redDeck.append(Card(c0))
        self.redDeck.append(Card(c1))
        self.redDeck.append(Card(c1))
        self.redDeck.append(Card(c2))
        self.redDeck.append(Card(c2))
        self.redDeck.append(Card(c3))
        self.redDeck.append(Card(c3))
        self.redDeck.append(Card(c4))
        self.redDeck.append(Card(c4))
        self.redDeck.append(Card(c4))
        self.redDeck.append(Card(c5))
        self.redDeck.append(Card(c5))
        self.redDeck.append(Card(c5))
        self.redDeck.append(Card(c6))
        self.redDeck.append(Card(c6))
        self.redDeck.append(Card(c7))
        self.redDeck.append(Card(c7))
        self.redDeck.append(Card(c7))
        self.redDeck.append(Card(c7))
        self.redDeck.append(Card(c8))
        self.redDeck.append(Card(c8))
        self.redDeck.append(Card(c9))
        self.redDeck.append(Card(c10))

    def set_up_yellowDeck(self):
        pass

    def set_up_greenDeck(self):
        pass

    def set_up_purpleDeck(self):
        pass

    """ GETTERS """

    def get_deck(self, color):
        if color == RED:
            self.get_redDeck()
        elif color == YELLOW:
            self.get_yellowDeck()
        elif color == PURPLE:
            self.get_purpleDeck()
        elif color == GREEN:
            self.get_greenDeck()
        else:
            raise Exception("something went wrong")

    def get_redDeck(self):
        return self.redDeck.copy()

    def get_yellowDeck(self):
        return self.yellowDeck.copy()

    def get_purpleDeck(self):
        return self.purpleDeck.copy()

    def get_greenDeck(self):
        return self.greenDeck.copy()
