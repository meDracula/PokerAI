from poker.dealer import Dealer


class Table:
    def __init__(self, players: dict):
        self.player_table = players
        self.players = []
        self.dealer = Dealer()
        self.community_cards = []

    def preflop(self):
        for player in self.player_table.values():
            player.hand = self.dealer.deal(2)
            self.players.append(player)

    def flop(self):
        self.community_cards = self.dealer.deal(3)

    def turn(self):
        self.community_cards += self.dealer.deal(1)

    def river(self):
        self.community_cards += self.dealer.deal(1)

    def player_fold(self, names):
        for player in filter(lambda player: player.name in names, self.players):
            self.players.remove(player)
            del player.hand

    def player_leave(self, names):
        for name in names:
            del self.player_table[name]

    def clear(self):
        self.players.clear()
        self.community_cards.clear()
        self.dealer.reset_deck()

    def __repr__(self):
        return f"{self.community_cards}"
