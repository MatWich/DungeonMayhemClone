import unittest
from classes.game_logic.Player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Palladin")

    def test_hand_refil(self):
        length = len(self.player.hand)
        self.player.draw_card()
        self.assertEqual(length, len(self.player.hand) - 1, "should be equal")

    def test_player_set_up(self):
        hp = 10
        actions = 1
        shield = 0

        self.player.set_up()

        self.assertEqual(self.player.hp, hp, "HP  SET UP TEST")
        self.assertEqual(self.player.actions, actions, "ACTIONS  SET UP TEST")
        self.assertEqual(self.player.shield, shield, "SHIELD  SET UP TEST")


    def test_take_damage(self):
        self.player.set_up()
        self.player.take_damage(5)
        self.assertEqual(self.player.hp, 5, "TAKE DAMAGE TEST")

    def test_is_dead(self):
        self.player.set_up()
        self.player.hp -= 10
        self.assertTrue(self.player.is_dead(), True)
        self.player.hp += 1
        self.assertFalse(self.player.is_dead(), False)

    def test_has_actions(self):
        self.player.set_up()
        self.assertEqual(self.player.actions, 1)
        self.player.play_card(0, Player("Palladin"))
        self.assertFalse(self.player.has_actions(), False)

    def test_is_deck_empty(self):
        self.player.set_up()
        deck_len = len(self.player.deck)
        for i in range(deck_len):
            self.player.draw_card()

        deck_len = len(self.player.deck)
        self.assertEqual(deck_len,0, "EMPTY DECK")
        self.player.renew_deck()
        deck_len = len(self.player.deck)
        self.assertEqual(deck_len, len(self.player.deck), "EMPTY DECK NO CARDS IN DISCARD PILE")

        self.player.play_card(0, Player("Palladin"))
        self.player.play_card(0, Player("Palladin"))
        self.player.play_card(0, Player("Palladin"))

        self.player.renew_deck()
        self.assertEqual(len(self.player.deck), 3, "RECREATING DECK FROM DISCARD PILE (3 cards in discard pile)")

    def test_new_test(self):
        self.player.set_up()
        self.player.play_card(0, Player("Palladin"))
        self.player.new_turn()
        self.assertEqual(self.player.actions, 1)


if __name__ == "__main__":
    unittest.main()

