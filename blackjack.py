'''
A SIMPLE BLACKJACK GAME
'''

import random
#List all the suits and ranks in a deck of cards. Creates a dictionary with ranks and their corresponding value
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
# Defines a card as having a suit and a rank
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    # Prints out the card
    def __str__(self):
        return self.rank + " of " + self.suit
# Defines a deck by iterating through all the suits and ranks, then adding to a list
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    # Prints out the deck
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return deck_comp
    # Shuffles the deck
    def shuffle(self):
        random.shuffle(self.deck)
    # Deals out a single card
    def deal(self):
        single_card = self.deck.pop()
        return single_card
# Defines a hand, starting as an empty list with no value
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    # Adds a card to the hand by passing in Deck.deal(), adds the value of the card, and counts aces
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        return card
    # If value of hand is over 21 and hand contains an ace, subtract 10
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
# Defines the amount of player chips as 100
class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
    # Adds the players bet to their total
    def win_bet(self):
        self.total += self.bet
    # Subtracts the players bet from their total
    def lose_bet(self):
        self.total -= self.bet
# Asks the player to place a bet (must be an integer) and ensures they have enough chips
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("\nPlease place a bet: "))
        except:
            print("Input must be an integer")
            continue
        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips. You're current total is {0}".format(chips.total))
            else:
                return f"Your current bet is {chips.bet}"
# If player hits, a card is dealt from the deck to the players hand and the value is adjusted for aces
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
# Asks player if they want to hit or stand, either calls hit method or passes to dealer
def hit_or_stand(deck,hand):
    global playing
    while True:
        choice = input("\nPlease enter 'h' to hit or 's' to stand: \n")
        if choice[0].lower() == "h":
            hit(deck,hand)
        elif choice[0].lower() == "s":
            print("\nPlayer Stands, Dealer's Turn")
            playing = False
        else:
            print("That is not a valid choice. Please enter 'h' to hit or 's' to stand: ")
            continue
        break
# Shows one of the dealers cards and all of the players cards
def show_some(player,dealer):
    print("\nDealers Cards: \n")
    print("<Card Hidden>", dealer.cards[1], sep=' | ')
    print("\nPlayers Cards: \n")
    print(*player.cards, player.value, sep=' | ')
# Shows all of the dealers and players cards
def show_all(player,dealer):
    print("\nDealers Cards: \n")
    print(*dealer.cards, dealer.value, sep=' | ')
    print("\nPlayers Cards: \n")
    print(*player.cards, player.value, sep=' | ')
# If player busts, they lose the bet
def player_busts(chips):
    chips.lose_bet()
    print("\nPLAYER BUSTS")
# If player wins, they win the bet
def player_wins(chips):
    chips.win_bet()
    print("\nPLAYER WINS")
# If dealer busts, player wins the bet
def dealer_busts(chips):
    chips.win_bet()
    print("\nDEALER BUSTS")
# If dealer wins, player loses the bet
def dealer_wins(chips):
    chips.lose_bet()
    print("\nDEALER WINS")
# If dealer and player tie, it's a push
def push():
    print("\nPUSH")
# Controls the flow of the game
playing = True
# Sets up the players chips
players_chips = Chips()
# Creates and shuffles the deck
game_deck = Deck()
game_deck.shuffle()
# Prints an opening statement
print("Welcome to Blackjack!\n")
# Starts the game
while True:
    # Creates the player and dealer hands and deals two cards to each
    players_hand = Hand()
    dealers_hand = Hand()
    dealers_hand.add_card(game_deck.deal())
    players_hand.add_card(game_deck.deal())
    dealers_hand.add_card(game_deck.deal())
    players_hand.add_card(game_deck.deal())
    dealers_hand.adjust_for_ace()
    players_hand.adjust_for_ace()
    # Asks the player to place their bet
    take_bet(players_chips)
    while playing:
        # Show cards except for one dealer card
        show_some(players_hand,dealers_hand)
        # Asks the player to hit or stand
        hit_or_stand(game_deck,players_hand)
        # If players hand exceeds 21, run player_busts(), show all cards, and break out of loop
        if players_hand.value > 21:
            show_all(players_hand,dealers_hand)
            player_busts(players_chips)
            break
    # If player hasn't busted, play dealers hand until dealer reaches 17
    if players_hand.value <= 21:
        while dealers_hand.value < 17:
            hit(game_deck,dealers_hand)
        # Show all cards
        show_all(players_hand,dealers_hand)
        # Run different winning scenarios
        if players_hand.value > dealers_hand.value:
            player_wins(players_chips)
        elif dealers_hand.value > 21:
            dealer_busts(players_chips)
        elif dealers_hand.value > players_hand.value:
            dealer_wins(players_chips)
        else:
            push()
    # Informs the player of their chips total
    print(f"\nYour chips total is {players_chips.total}\n")
    # Ask to play again
    replay = input("Would you like to continue playing? y or n: ")
    if replay[0].lower() == "y":
        playing = True
        continue
    else:
        print("\nThanks for playing!")
        break
