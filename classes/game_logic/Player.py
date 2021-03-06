try:
    from classes.game_logic.Card import Card
    from classes.game_logic.Data import Data
    import random
except ImportError as ex:
    raise ImportError("Cannot import all modules")


class Player:
    def __init__(self, color, name="BOT"):      # color refers to the deck that this player will be using
        self.color = color
        self.data = Data.get_instance()
        self.hand = []
        # this will be replaced by global list with cards by using .copy() method
        self.deck = self.data.get_deck(self.color)
        self.discardPile = []
        self.hp = None
        self.shield = None
        self.actions = None
        self.name = name
        self.set_up()

    def set_up(self):
        self.hp = 10
        self.shield = 0
        self.actions = 1

        for i in range(3):
            self.draw_card()

    def draw_card(self):
        index = random.randint(0, len(self.deck) - 1)
        self.hand.append(self.deck[index])
        self.deck.pop(index)

    def play_card(self, index, target):
        card = self.hand[index]
        print(card)
        '''action of the card'''
        if card.attack:
            target.take_damage(card.attack)
        if card.actions:
            self.actions += card.actions
        if card.draw != 0:
            for i in range(card.draw):
                self.draw_card()
        if card.heal:
            self.hp += card.heal
            if self.hp > 10:
                self.hp = 10
        if card.shield != 0:
            self.shield += card.shield
        '''end of action of the card'''
        self.discardPile.append(card)
        self.hand.pop(index)
        self.actions -= 1

    def check_hand_overflow(self):
        return True if len(self.hand) >= 6 else False

    """ RECREATING DECK """
    def is_deck_empty(self):
        return True if len(self.deck) == 0 else False

    def renew_deck(self):
        if self.is_deck_empty():
            self.deck = self.discardPile.copy()
            self.discardPile.clear()

    def take_damage(self, amount):
        if self.shield:
            if self.shield >= amount:
                self.shield -= amount
            else:
                diff = abs(self.shield - amount)
                self.shield = 0
                self.hp -= diff
        else:
            self.hp -= amount

        if self.is_dead():
            print(f"player {self.color} died.")
            return
        """ do stuff when he is defeated maybe returns 
        a value to trigger the back to menu option"""

    def is_dead(self):
        return True if self.hp <= 0 else False

    def has_actions(self):
        return True if self.actions > 0 else False

    """ HELPERS """
    def show_hand(self):
        for index, card in enumerate(self.hand):
            print(f"{index}.{card}")

    def summary(self):
        print(f"HP: {self.hp}, SHIELD: {self.shield} HAND: {len(self.hand)} ACTIONS: {self.actions}")

    def new_turn(self):
        self.draw_card()
        self.actions = 1

    def refil_hand(self):
        for i in range(3):
            self.draw_card()

    def is_empty_hand(self):
        return True if len(self.hand) == 0 else False