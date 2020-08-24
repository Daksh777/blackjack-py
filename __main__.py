import random

from deck import Deck
from player import Player, Computer

def play_turn(player):
    print(player.name + '\'s Turn!')
    choice = player.input()
    print(player.name, 'chose', choice)
    print('-'*40)

if __name__ == "__main__":
    deck = Deck()

    player = Player()
    comp = Computer()

    while player.balance > 0:
        play_turn(player)
        # game logic needed
        
