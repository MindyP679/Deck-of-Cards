from random import shuffle


class Card():

    def __init__(self, val, suit):
        self.val = val
        self.suit = suit
        
    def __repr__(self):
        return f"{self.val} of {self.suit}"

class Deck():

    def __init__(self):
        values = ("A", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "J", "Q", "K")
        suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        self.cards = [Card(val, suit)
                      for val in values for suit in suits]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def __iter__(self): #Makes deck iterable
        for card in self.cards:
            yield card

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt.")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)
