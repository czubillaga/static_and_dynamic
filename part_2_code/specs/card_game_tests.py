import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card(1, 1)
        self.card2 = Card(2, 2)
        self.card3 = Card(3, 3)
        self.cards = [self.card1, self.card2, self.card3]
        self.game = CardGame()
    
    def test_check_for_ace__true(self):
        self.assertEqual(True, self.game.check_for_ace(self.card1))

    def test_check_for_ace__false(self):
        self.assertEqual(False, self.game.check_for_ace(self.card2))

    def test_highest_card(self):
        self.assertEqual(self.card2.value, self.game.highest_card(self.card1, self.card2).value)

    def test_cards_total(self):
        self.assertEqual('You have a total of 6', self.game.cards_total(self.cards))