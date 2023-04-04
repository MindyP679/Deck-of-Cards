import unittest
from deck_of_cards import Card, Deck

class CardTests(unittest.TestCase):
	def setUp(self):
		self.my_card = Card("A", "Hearts")

	def test_card(self):
		self.assertEqual(repr(self.my_card), "A of Hearts")

class DeckTests(unittest.TestCase):
	def setUp(self):
		self.deck_1 = Deck()

	def test_count(self):
		self.deck_1.count()
		self.assertEqual(len(self.deck_1.cards), 52)

	def test_shuffle(self):
		self.deck_1.shuffle()
		self.deck_2 = Deck()
		self.assertNotEqual(self.deck_1.cards, self.deck_2.cards)
		self.assertEqual(len(self.deck_1.cards),len(self.deck_1.cards))

	def test_deal_card(self):
		self.assertEqual(self.deck_1.cards[-1],self.deck_1.deal_card())
		self.assertEqual(len(self.deck_1.cards),51)

	def test_deal_hand(self):
		self.assertEqual(self.deck_1.cards[-3:],self.deck_1.deal_hand(3))
		self.assertEqual(len(self.deck_1.cards),49)

if __name__ == "__main__":
    unittest.main()