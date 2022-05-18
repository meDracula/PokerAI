from random import shuffle

class Dealer:
    def __init__(self):
        self.deck = Dealer.init_deck()

    def deal(self):
        return self.deck.pop(0)

    @staticmethod
    def init_deck():
        deck = ["Q", "K", "A"]
        shuffle(deck)
        return deck
