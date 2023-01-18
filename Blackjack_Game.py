# Import Modules and Define Variables
import time 
import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")

ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, 
            "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

playing = True 

#Classes

class Card: # Creates all the cards
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank 

    def __str__(self):
        return self.rank + " of " + self.suit 

class Deck: # Creates a deck of cards

    def __init__(self):
        self.deck = [] # have not created a deck yet 
        for suit in suits: # add 52 cards to the deck 
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ""
        for card in self.deck: 
            deck_comp += "\n" + card.__str__()
        return "The deck has: " + deck_comp
    
    def shuffle(self): # shuffle all the cards in the deck
        random.shuffle(self.deck)

    def deal(self): #pick out a card from the deck
        single_card = self.deck.pop()
        return single_card 

class Hand: # show all the cards that the dealer and player have 

    def __init__(self):
        self.cards = [] 
        self.value = 0
        self.aces = 0 # keep track of aces 

    def add_card(self, card):  # add a card to the player's or dealer's head 
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1 

    def adjust_for_ace(self): # whenever a score is over 21 and a player has an ace in their hand, adjust their score 
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

def hit(deck, hand): # adds a card to a player's hand and adjusts their score if needed 
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing 

    while True:
        ask = input("\nWould you like to (H)it or (S)tand? Please enter 'H' or 'S': ")
        time.sleep(1)
        if ask[0].lower() == "h":
            hit(deck, hand)
            if hand.value == 21:
                playing = False 
        elif ask[0].lower() == "s":
            print("Player stands, Dealer is playing.")
            playing = False
        else:
            print("I'm sorry! I did not understand that! Please try again!")
            continue 
        break 


def show_player(player):
    print("\nPlayer's Hand: ", *player.cards, sep="\n ")
    print("Player Score: " + str(player.value))

def show_dealer(dealer):
    print("\nDealer has: ", *dealer.cards, sep="\n ")
    print("Dealer Score: " + str(dealer.value))

def show_partial(player, dealer):
    print("\nDealer has: ")
    print("", dealer.cards[0])
    print(" ?")
    print("\nPlayer has", *player.cards, sep="\n ")
    print("Player score: " + str(player.value))


def show_full(player, dealer):
    print("\nDealer's Hand: ", *dealer.cards, sep="\n ")
    print("Dealer's Score: ", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep="\n ")
    print("Player's Score: ", player.value)

while True:
    print("\nWelcome to Blackjack!")

    # create and shuffle deck
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    # if player is given two aces make sure to adjust for it 
    player_hand.adjust_for_ace()

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
     # if dealer is given two aces make sure to adjust for it 
    dealer_hand.adjust_for_ace()

    # if the player starts with 21, it's an automatic win 
    if player_hand.value == 21:
        playing = False 
    else:
    # show cards
        show_partial(player_hand, dealer_hand)

    while playing: 
        hit_or_stand(deck, player_hand)
        if player_hand.value != 21 and playing:
            show_partial(player_hand, dealer_hand)

        if player_hand.value > 21:
            print("\nPLAYER BUSTS!")
            break
    
    # player automatically wins if they reach 21 
    if player_hand.value == 21:
        show_full(player_hand, dealer_hand)
        print("\nPlayer Wins!")
        print("Blackjack!")

    elif player_hand.value < 21:

        show_dealer(dealer_hand)

        while dealer_hand.value < 17:
            time.sleep(1)
            hit(deck, dealer_hand)
            show_dealer(dealer_hand)
        
        time.sleep(1)
        show_player(player_hand)

        if dealer_hand.value > 21:
            print("\nDEALER BUSTS!")
        
        elif dealer_hand.value > player_hand.value:
            print("\nDEALER WINS!")
        
        elif dealer_hand.value < player_hand.value:
            print("\nPLAYER WINS!")
        
        elif dealer_hand.value == player_hand.value:
            print("\nDEALER AND PLAYER TIE!")
    
    # gives you the option to play again 
    new_game = input("\nWould you like to play again? Enter 'y' or 'n': ")
    if new_game[0].lower() == "y":
        playing = True 
        continue 
    else:
        print("\nThanks for playing!")
        break 


# only want to run this code from the main file 
if __name__ == '__main__':
    pass

