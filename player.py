from random import randint


class PlayerBase:
    def __init__(self):
        self.balance = 100

    def input(self):
        raise NotImplementedError()

    def bid(self, amount):
        if amount > self.balance:
            raise ValueError('Amount greater than what you have')

        self.balance -= amount

    def win(self, amount):
        self.balance += amount


class Player(PlayerBase):
    def __init__(self):
        super().__init__()
        self.name = 'Player'

    def input(self):
        return int(input('> '))

class Computer(PlayerBase):
    def __init__(self):
        super().__init__()
        self.name = 'Computer'

    def input(self):
        choice = randint(1, 2)
        print('>', choice)
        return choice
