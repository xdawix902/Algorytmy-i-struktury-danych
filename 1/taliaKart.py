import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class PolishDeck:
    ranks = [str(n) for n in range(2, 11)] + list('WDKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index]

exemplar_card = Card('7', 'diamonds')
print(exemplar_card)