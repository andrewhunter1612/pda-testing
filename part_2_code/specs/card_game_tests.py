import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def test_check_for_ace(self):
        ace_card = Card("Spades", 1)
        self.assertEqual(True, CardGame().check_for_ace(ace_card))

    def test_highest_card(self):
        card_1 = Card("Hearts", 4)
        card_2 = Card("Spades", 1)
        self.assertEqual(card_1, CardGame().highest_card(card_1, card_2))

    def test_cards_total(self):
        card_1 = Card("Hearts", 4)
        card_2 = Card("Spades", 1)
        cards_list = [card_1, card_2]
        self.assertEqual("You have a total of 5", CardGame().cards_total(cards_list))