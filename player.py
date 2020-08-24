from random import randint


class NotEnoughBalanceException(Exception):
    """Raised when the player tries to bid more than his balance"""

class PlayerBase:
    def __init__(self):
        self.hand = []

    def pick(self, card):
        self.hand.append(card)

    def clear(self):
        self.hand = []

    def print_hand(self):
        for i, card in enumerate(self.hand, 1):
            print(f'{i}. {card.name}')

class Player(PlayerBase):
    def __init__(self):
        super().__init__()
        self.balance = 100
        self.name = 'Player'

    def input(self):
        choice = int(input('> '))
        return choice == 1

    def bid(self, amount):
        if amount > self.balance:
            raise NotEnoughBalanceException('Amount greater than what you have')

        self.balance -= amount

    def win(self, amount):
        self.balance += amount

class Computer(PlayerBase):
    def __init__(self):
        super().__init__()
        self.name = 'Computer'

    def input(self):
        choice = randint(1, 2)
        print('>', choice)
        return choice == 1
