import random
class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for face in ['Ace', *range(2, 10), 'Jack', 'Queen', 'King']:
                name = f'{face} of {suit}'
                if isinstance(face, str):
                    value = 10
                else:
                    value = face
                self.cards.append(Card(name, value))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def print_cards(self):
        for card in self.cards:
            print(card.name)

    def pick_one(self):
        return self.cards.pop(0)


class Card:
    def __init__(self, name, value):
        self.name = name
        self.value = value
