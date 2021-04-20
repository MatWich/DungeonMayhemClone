try:
    from classes.game_logic.Data import Data
    from classes.game_logic.Player import Player
    import random
    from config import *
except ImportError:
    raise ImportError("Cannot import all modules")

if __name__ == '__main__':
    d = Data()
    p1 = Player(RED)
    p2 = Player(RED)
    counter = 0
    while not p1.is_dead() and not p2.is_dead():
        if counter % 2 == 0:
            p1.show_hand()
            index = int(input("Choose Card: "))
            p1.play_card(index, p2)
            if p1.has_actions():
                continue
        else:
            #p2.show_hand()
            index = random.randint(0, len(p2.hand) - 1)
            p2.play_card(index, p1)
            if p2.has_actions():
                continue


        p1.summary()
        p2.summary()
        p1.actions = 1
        p2.actions = 1
        counter += 1
        p2.draw_card()
        p1.draw_card()
        print()