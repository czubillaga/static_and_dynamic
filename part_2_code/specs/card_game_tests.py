import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card(1, 1)
        self.card2 = Card(2, 2)
        self.card3 = Card(3, 3)
    
    def test_check_for_ace__true(self):
        self.assertEqual(True, CardGame.check_for_ace(self.card1))