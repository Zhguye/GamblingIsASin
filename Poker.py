import random

STRAIGHT_FLUSH = 8
FOUR_OF_A_KIND = 7
FULL_HOUSE = 6
FLUSH = 5
STRAIGHT = 4
THREE_OF_A_KIND = 3
TWO_PAIRS = 2
PAIR = 1
HIGH = 0

RESULTSTRINGS = ["high card", "a pair", "two pairs",
                 "three of a kind", "straight", "flush",
                 "full house", "four of a kind", "straight flush"]

SPADE = "\u2660"
HEART = "\u2661"
DIAMOND = "\u2662"
CLUB = "\u2663"

SUITS = [SPADE, HEART, DIAMOND, CLUB]
FACES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
FACES_AS_VALUES = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13,
                   "A": 14}



def initialize_random():
    seed = random.randint(0,1024)
    random.seed(seed)


def initialize_deck():
    deck = []
    for face in FACES:
        for suit in SUITS:
            card = [face, suit]
            deck.append(card)
    return deck


def shuffle_and_deal(deck):
    random.shuffle(deck)
    player_hand = []
    computer_hand = []
    for i in range(5):
        player_hand.append(deck.pop())
        computer_hand.append(deck.pop())
    return deck, player_hand, computer_hand
