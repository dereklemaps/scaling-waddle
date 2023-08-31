from random import shuffle

suits = ('Spades', 'Clubs', 'Diamonds', 'Hearts')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
class Deck:

    def __init__ (self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(rank,suit)
                self.all_cards.append(created_card)
    
    def shuffle_cards(self):
        shuffle(self.all_cards)
        print('Deck has been shuffled')
    
    def deal_one(self):
        try:
            return self.all_cards.pop()
        except:
            return 'No cards left'
        
class Player:
    
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_card(self):
        return self.all_cards.pop(0)

    def add_card(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'

player1 = Player('One')
player2 = Player('Two')

newdeck = Deck()
newdeck.shuffle_cards()

for i in range(26):
    player1.add_card(newdeck.deal_one())
    player2.add_card(newdeck.deal_one())

game_on = True

round_num = 0
while game_on:
    round_num += 1
    print(f'Round {round_num}')

    if len(player1.all_cards) == 0:
        print('Player Two wins!')
        game_on = False
    elif len(player2.all_cards) == 0:
        print('Player One wins!')
        game_on = False
    
    player_one_cards = []
    player_one_cards.append(player1.remove_card())
    player_two_cards = []
    player_two_cards.append(player2.remove_card())

    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player1.add_card(player_one_cards)
            player1.add_card(player_two_cards)
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player2.add_card(player_one_cards)
            player2.add_card(player_two_cards)
            at_war = False
        else:
            print('WAR!')
            if len(player1.all_cards) < 10:
                print('Player One does not have enough cards. Player Two wins!')
                game_on = False
                break
            elif len(player2.all_cards) < 10:
                print('Player Two does not have enough cards. Player One wins!')
                game_on = False
                break
            else:
                for each in range(10):
                    player_one_cards.append(player1.remove_card())
                    player_two_cards.append(player2.remove_card())
