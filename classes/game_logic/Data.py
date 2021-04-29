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
        self.started = False
        self.textHistory = ""

        self.set_up()

    def set_up(self):
        self.set_up_redDeck()
        self.set_up_greenDeck()
        self.set_up_purpleDeck()
        self.set_up_yellowDeck()

    def set_up_redDeck(self):
        # 3
        c0 = {"name": "For Juistice!",
              "attack": 1,
              "actions": 1,
              "draw": 0,
              "heal": 0,
              "shield": 0,
              "image": os.path.join(RED_DECK_DIR, "For_Juistice.png")}
        # 2
        c1 = {"name": "For The Most Juistice!",
              "attack": 3,
              "actions": 0,
              "draw": 0,
              "heal": 0,
              "shield": 0,
              "image": os.path.join(RED_DECK_DIR, "For_The_Most_Juistice.png")}
        # 2
        c2 = {"name": "Finger-wag of Judgment",
              "attack": 0,
              "actions": 2,
              "draw": 0,
              "heal": 0,
              "shield": 0,
              "image": os.path.join(RED_DECK_DIR, "Finger-Wag_Of_Judgement.png")}
        # 2
        c3 = {"name": "Spinning Parry",
              "attack": 0,
              "actions": 0,
              "draw": 1,
              "heal": 0,
              "shield": 1,
              "image": os.path.join(RED_DECK_DIR, "Spinning_Parry.png")}
        # 3
        c4 = {"name": "Fighting Words",
              "attack": 2,
              "actions": 0,
              "draw": 0,
              "heal": 1,
              "shield": 0,
              "image": os.path.join(RED_DECK_DIR, "Fighting_Words.png")}
        # 3
        c5 = {"name": "Divine Smite",
              "attack": 3,
              "actions": 0,
              "draw": 0,
              "heal": 1,
              "shield": 0,
              "image": os.path.join(RED_DECK_DIR, "Divine_Smite.png")}
        # 2
        c6 = {"name": "High Charisma",
              "attack": 0,
              "actions": 0,
              "draw": 2,
              "heal": 0,
              "shield": 0,
              "image": os.path.join(RED_DECK_DIR, "High_Charisma.png")}
        # 4
        c7 = {"name": "For Even More Juistice!",
              "attack": 2,
              "actions": 0,
              "draw": 0,
              "heal": 0,
              "shield": 0,
              "image": os.path.join(RED_DECK_DIR, "For_Even_More_Juistice.png")}
        # 2
        c8 = {"name": "Divine Shield",
              "attack": 0,
              "actions": 0,
              "draw": 0,
              "heal": 0,
              "shield": 3,
              "image": os.path.join(RED_DECK_DIR, "Divine_Shield.png")}
        # 1
        c9 = {"name": "Fluffy",
              "attack": 0,
              "actions": 0,
              "draw": 0,
              "heal": 0,
              "shield": 2,
              "image": os.path.join(RED_DECK_DIR, "Fluffy.png")}
        # 1
        c10 = {"name": "Cure Wounds",
               "attack": 0,
               "actions": 0,
               "draw": 2,
               "heal": 1,
               "shield": 0,
               "image": os.path.join(RED_DECK_DIR, "Cure_Wounds.png")}

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
        c0 = {"name": "Evil Sneer",
              "attack": 0,
              "actions": 1,
              "draw": 0,
              "heal": 1,
              "shield": 0,
              "image": os.path.join(YELLOW_DECK_DIR, "Evil_Sneer.png")}  # 2

        c1 = {"name": "Lighting Bolt",
              "attack": 3,
              "actions": 0,
              "draw": 0,
              "heal": 0,
              "shield": 0,
              "image": os.path.join(YELLOW_DECK_DIR, "Lightning_Bolt.png")}  # 4

        c2 = {"name": "Mirror Image",
              "attack": 0,
              "actions": 0,
              "draw": 0,
              "heal": 0,
              "shield": 3,
              "image": os.path.join(YELLOW_DECK_DIR, "Mirror_Image.png")}  # 1

        c3 = {"name": "Stoneskin",
              "attack": 0,
              "actions": 0,
              "draw": 0,
              "heal": 0,
              "shield": 2,
              "image": os.path.join(YELLOW_DECK_DIR, "Stoneskin.png")}  # 1

        c4 = {"name": "Speed Of Thought",
              "attack": 0,
              "actions": 2,
              "draw": 0,
              "heal": 0,
              "shield": 0,
              "image": os.path.join(YELLOW_DECK_DIR, "Speed_Of_Thought.png")}  # 3

        c5 = {"name": "Magic Missile",
              "attack": 1,
              "actions": 1,
              "draw": 0,
              "heal": 0,
              "shield": 0,
              "image": os.path.join(YELLOW_DECK_DIR, "Magic_Missile.png")}  # 3

        c6 = {"name": "Burning Hands",
              "attack": 2,
              "actions": 0,
              "draw": 0,
              "heal": 0,
              "shield": 0,
              "image": os.path.join(YELLOW_DECK_DIR, "Burning_Hands.png")}  # 3

        c7 = {"name": "Shield",
              "attack": 0,
              "actions": 0,
              "draw": 1,
              "heal": 0,
              "shield": 1,
              "image": os.path.join(YELLOW_DECK_DIR, "Shield.png")}  # 2

        c8 = {"name": "Knowledge Is Power",
              "attack": 0,
              "actions": 0,
              "draw": 3,
              "heal": 0,
              "shield": 0,
              "image": os.path.join(YELLOW_DECK_DIR, "Knowledge_Is_Power.png")}  # 3

        self.yellowDeck.append(Card(c0))
        self.yellowDeck.append(Card(c0))
        self.yellowDeck.append(Card(c1))
        self.yellowDeck.append(Card(c1))
        self.yellowDeck.append(Card(c1))
        self.yellowDeck.append(Card(c1))
        self.yellowDeck.append(Card(c2))
        self.yellowDeck.append(Card(c3))
        self.yellowDeck.append(Card(c4))
        self.yellowDeck.append(Card(c4))
        self.yellowDeck.append(Card(c4))
        self.yellowDeck.append(Card(c5))
        self.yellowDeck.append(Card(c5))
        self.yellowDeck.append(Card(c5))
        self.yellowDeck.append(Card(c6))
        self.yellowDeck.append(Card(c6))
        self.yellowDeck.append(Card(c6))
        self.yellowDeck.append(Card(c7))
        self.yellowDeck.append(Card(c7))
        self.yellowDeck.append(Card(c8))
        self.yellowDeck.append(Card(c8))
        self.yellowDeck.append(Card(c8))

    def set_up_greenDeck(self):
        c0 = {"name": "Bag Of Rats",
              "attack": 0,
              "actions": 0,
              "draw": 1,
              "heal": 0,
              "shield": 1,
              "image": os.path.join(GREEN_DECK_DIR, "Bag_Of_Rats.png")}
        self.greenDeck.append(Card(c0))

        c1 = {"name": "Riff",
              "attack": 0,
              "actions": 0,
              "draw": 0,
              "heal": 0,
              "shield": 3,
              "image": os.path.join(GREEN_DECK_DIR, "Riff.png")}
        self.greenDeck.append(Card(c1))
        self.greenDeck.append(Card(c1))

        c2 = {"name": "Spiked Shield",
              "attack": 0,
              "actions": 0,
              "draw": 0,
              "heal": 0,
              "shield": 2,
              "image": os.path.join(GREEN_DECK_DIR, "Spiked_Shield.png")}
        self.greenDeck.append(Card(c2))

        c3 = {"name": "Flex",
              "attack": 0,
              "actions": 0,
              "draw": 1,
              "heal": 1,
              "shield": 0,
              "image": os.path.join(GREEN_DECK_DIR, "Flex.png")}
        self.greenDeck.append(Card(c3))
        self.greenDeck.append(Card(c3))

        c4 = {"name": "Snack Time",
              "attack": 0,
              "actions": 0,
              "draw": 2,
              "heal": 1,
              "shield": 0,
              "image": os.path.join(GREEN_DECK_DIR, "Snack_Time.png")}
        self.greenDeck.append(Card(c4))

        c5 = {"name": "Open The Armory",
              "attack": 0,
              "actions": 0,
              "draw": 2,
              "heal": 0,
              "shield": 0,
              "image": os.path.join(GREEN_DECK_DIR, "Open_The_Armory.png")}
        self.greenDeck.append(Card(c5))
        self.greenDeck.append(Card(c5))

        c6 = {"name": "RAGE !",
              "attack": 4,
              "actions": 0,
              "draw": 0,
              "heal": 0,
              "shield": 0,
              "image": os.path.join(GREEN_DECK_DIR, "Rage.png")}
        self.greenDeck.append(Card(c6))
        self.greenDeck.append(Card(c6))

        c7 = {"name": "Brutal Punch",
              "attack": 2,
              "actions": 0,
              "draw": 0,
              "heal": 0,
              "shield": 0,
              "image": os.path.join(GREEN_DECK_DIR, "Brutal_Punch.png")}
        self.greenDeck.append(Card(c7))
        self.greenDeck.append(Card(c7))

        c8 = {"name": "Big Axe Is Best Axe",
              "attack": 3,
              "actions": 0,
              "draw": 0,
              "heal": 0,
              "shield": 0,
              "image": os.path.join(GREEN_DECK_DIR, "Big_Axe_Is_Best_Axe.png")}
        self.greenDeck.append(Card(c8))
        self.greenDeck.append(Card(c8))
        self.greenDeck.append(Card(c8))
        self.greenDeck.append(Card(c8))
        self.greenDeck.append(Card(c8))

        c9 = {"name": "Head Butt",
              "attack": 1,
              "actions": 1,
              "draw": 0,
              "heal": 0,
              "shield": 0,
              "image": os.path.join(GREEN_DECK_DIR, "Head_Butt.png")}
        self.greenDeck.append(Card(c9))
        self.greenDeck.append(Card(c9))

        c10 = {"name": "Two Axes Are Better Than One",
               "attack": 0,
               "actions": 2,
               "draw": 0,
               "heal": 0,
               "shield": 0,
               "image": os.path.join(GREEN_DECK_DIR, "Two_Axes_are_Better_Than_One.png")}
        self.greenDeck.append(c10)
        self.greenDeck.append(c10)

    def set_up_purpleDeck(self):
        c0 = {"name": "My Little Friend",
              "attack": 0,
              "actions": 0,
              "draw": 0,
              "heal": 0,
              "shield": 3,
              "image": os.path.join(PURPLE_DECK_DIR, "My_Little_Friend.png")}
        self.purpleDeck.append(Card(c0))

        c1 = {"name": "Stolen Potion",
              "attack": 0,
              "actions": 1,
              "draw": 0,
              "heal": 1,
              "shield": 0,
              "image": os.path.join(PURPLE_DECK_DIR, "Stolen_Potion.png")}
        self.purpleDeck.append(Card(c1))
        self.purpleDeck.append(Card(c1))

        c2 = {"name": "Cunning Action",
              "attack": 0,
              "actions": 2,
              "draw": 0,
              "heal": 0,
              "shield": 0,
              "image": os.path.join(PURPLE_DECK_DIR, "Cunning_Action.png")}
        self.purpleDeck.append(Card(c2))
        self.purpleDeck.append(Card(c2))

        c3 = {"name": "The Goon Squad",
              "attack": 0,
              "actions": 0,
              "draw": 0,
              "heal": 0,
              "shield": 2,
              "image": os.path.join(PURPLE_DECK_DIR, "The_Goon_Squad.png")}
        self.purpleDeck.append(Card(c3))
        self.purpleDeck.append(Card(c3))

        c4 = {"name": "One Thrown Dagger",
              "attack": 1,
              "actions": 1,
              "draw": 0,
              "heal": 0,
              "shield": 0,
              "image": os.path.join(PURPLE_DECK_DIR, "One_Thrown_Dagger.png")}
        self.purpleDeck.append(Card(c4))
        self.purpleDeck.append(Card(c4))
        self.purpleDeck.append(Card(c4))
        self.purpleDeck.append(Card(c4))
        self.purpleDeck.append(Card(c4))

        c5 = {"name": "Two Thrown Daggers",
              "attack": 2,
              "actions": 0,
              "draw": 0,
              "heal": 0,
              "shield": 0,
              "image": os.path.join(PURPLE_DECK_DIR, "Two_Thrown_Daggers.png")}
        self.purpleDeck.append(Card(c5))
        self.purpleDeck.append(Card(c5))
        self.purpleDeck.append(Card(c5))
        self.purpleDeck.append(Card(c5))

        c6 = {"name": "Winged Serpent",
              "attack": 0,
              "actions": 0,
              "draw": 1,
              "heal": 0,
              "shield": 1,
              "image": os.path.join(PURPLE_DECK_DIR, "Winged_Serpent.png")}
        self.purpleDeck.append(Card(c6))
        self.purpleDeck.append(Card(c6))

        c7 = {"name": "Even More Daggers",
              "attack": 0,
              "actions": 0,
              "draw": 2,
              "heal": 1,
              "shield": 0,
              "image": os.path.join(PURPLE_DECK_DIR, "Even_More_Daggers.png")}
        self.purpleDeck.append(Card(c7))

        c8 = {"name": "All The Thrown Daggers",
              "attack": 3,
              "actions": 0,
              "draw": 0,
              "heal": 0,
              "shield": 0,
              "image": os.path.join(PURPLE_DECK_DIR, "All_The_Thrown_Daggers.png")}
        self.purpleDeck.append(Card(c8))
        self.purpleDeck.append(Card(c8))
        self.purpleDeck.append(Card(c8))

    """ GETTERS """

    def get_deck(self, color):
        if color == RED:
            return self.redDeck.copy()
        elif color == YELLOW:
            return self.yellowDeck.copy()
        elif color == PURPLE:
            return self.purpleDeck.copy()
        elif color == GREEN:
            return self.greenDeck.copy()
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
