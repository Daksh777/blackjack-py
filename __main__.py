from deck import Deck
from player import Player, Computer, NotEnoughBalanceException

def play_round(player, deck):
    print(player.name + '\'s Turn!\n')
    player.pick(deck.get_one())
    player.pick(deck.get_one())
    while True:
        player.print_hand()
        card_sum = sum(card.value for card in player.hand)
        print('Total: ', card_sum)
        print()

        bust = card_sum > 21
        if bust:
            print('OH NO! you got BUSTED!')
            break

        print('Choose:')
        print('1. Hit, or 2. Stand')
        hit = player.input()
        if hit:
            player.pick(deck.get_one())
        else:
            break
    player.clear()
    
    print(player.name + '\'s total sum was:', 'BUST!' if bust else card_sum)

    return -1 if bust else card_sum

if __name__ == "__main__":
    deck = Deck()

    player = Player()
    comp = Computer()
    _round = 1

    while player.balance > 0:
        print('ROUND', _round)
        print('The player\'s balance is', player.balance)

        while True:
            try:
                print('Enter the bidding amount.')
                bid_amount = int(input('> '))
                player.bid(bid_amount)
                break
            except NotEnoughBalanceException:
                print('You don\'t have enough balance for this')
            except ValueError:
                print('Try again')
            except KeyboardInterrupt:
                exit()
        
        print(f'Starting Round {_round}:')
        try:
            player_score = play_round(player, deck)
            input('Press any key to continue.')
            print('--------------------')
            comp_score = play_round(comp, deck)
        except KeyboardInterrupt:
            exit()

        if player_score > comp_score:
            print('Player won this round!')
            player.balance += 2 * bid_amount
        elif player_score < comp_score:
            print('Player lost this round.')
        else:
            print('This round was a draw.')
            player.balance += bid_amount

        try:
            input('Press any key to continue.')
        except KeyboardInterrupt:
            exit()

        print('--------------------')
        _round += 1

    print('Looks like you\'ve lost all your balance.')
    print('Play again for a better luck!')
