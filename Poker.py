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
  def check_line(line):
    try:
        linelist = line.split(",")
        newlinelist = []
        for i in range(len(linelist)):
            newlinelist.append(int(linelist[i]))
        for i in newlinelist:
            if i > 5:
                newlinelist.remove(i)
            if i<1:
                newlinelist.remove(i)
        newlinelist = list(dict.fromkeys(newlinelist))
        return newlinelist
    except ValueError:
        return line

def draw_more(deck, hand, line):
    #check_line(line)
    #deck, newhand, comp_hand = shuffle_and_deal(deck)
    line_list = check_line(line)
    for number in line_list:
        hand[int(number) - 1] = deck.pop()
    return deck, hand


def print_hand(hand):
    rows = len(hand)
    columns = len(hand[0])
    resultrow = ""
    for i in range(rows):
        for j in range(columns):
            resultrow += "{}".format(hand[i][j])
        resultrow += " "
    print(resultrow)

def has_straight_flush(hand):
    temp = []
    boolean, number = has_straight(hand)
    boolean2, number2 = has_flush(hand)
    if boolean == True and boolean2 == True:
        for i in range(len(hand)):
            temp.append(FACES_AS_VALUES[hand[i][0]])
        temp = sorted(temp)
        if temp[0] + 4 == temp[1] + 3 == temp[2] + 2 == temp[3] + 1 == temp[4]:
            return True, temp[4]
    else:
        return False, None

def has_four_of_a_kind(hand):
    temp = []
    for card in hand:
        temp.append(card[0])
    for face in FACES:
        if temp.count(face) == 4:
            return True, FACES_AS_VALUES[face]
    return False, None


def has_full_house(hand):
    res1, high1 = has_pair(hand)
    res2, high2 = has_three_of_a_kind(hand)
    if res1 and res2:
        return True, high2
    return False, None

def has_flush(hand):
    temp = []
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
        for i in range(len(hand)):
            temp.append(FACES_AS_VALUES[hand[i][0]])
        temp = sorted(temp)
        return True, temp[4]
    else:
        return False, None

def has_straight(hand):
    temp = []
    for i in range(len(hand)):
        temp.append(FACES_AS_VALUES[hand[i][0]])
    temp = sorted(temp)
    if (temp[0] + 4) == (temp[1] + 3) == (temp[2] + 2) == (temp[3] + 1) == temp[4]:
        return True, temp[4]
    else:
        return False, None

def has_three_of_a_kind(hand):
    temp = []
    for i in range(len(hand)):
        temp.append(hand[i][0])
    for face in FACES:
        if temp.count(face) == 3:
            return True, FACES_AS_VALUES[face]
    return False, None


def has_two_pairs(hand):

    faces_in_hand = []
    for i in range(len(hand)):
        faces_in_hand.append(hand[i][0])
    for first_face in FACES:
        if faces_in_hand.count(first_face) == 2:
            for second_face in FACES:
                if faces_in_hand.count(second_face) == 2:
                    if first_face != second_face:
                        rank_card = max(FACES_AS_VALUES[first_face], FACES_AS_VALUES[second_face])
                        return True, rank_card
    return False, None


def has_pair(hand):
    temp = []
    for i in range(len(hand)):
        temp.append(hand[i][0])
    for face in FACES:
        if temp.count(face) == 2:
            return True, FACES_AS_VALUES[face]
    return False, None


def highest_card(hand):
    temp = []
    for i in range(len(hand)):
        temp.append(FACES_AS_VALUES[hand[i][0]])
    temp = sorted(temp)
    return temp[4]


def check_hand(hand):
    # This codes simply checks for all possibilities of combinations. If it finds none, it returns the higest card

    if has_straight_flush(hand)[0]:
        i,j = has_straight_flush(hand)
        return STRAIGHT_FLUSH, j
    if has_four_of_a_kind(hand)[0]:
        i, j = has_four_of_a_kind(hand)
        return FOUR_OF_A_KIND, j
    if has_full_house(hand)[0]:
        i, j = has_full_house(hand)
        return FULL_HOUSE, j
    if has_flush(hand)[0]:
        i,j = has_flush(hand)
        return FLUSH, j
    if has_straight(hand)[0]:
        i,j = has_straight(hand)
        return STRAIGHT, j
    if has_three_of_a_kind(hand)[0]:
        i,j = has_three_of_a_kind(hand)
        return THREE_OF_A_KIND, j
    if has_two_pairs(hand)[0]:
        i,j = has_two_pairs(hand)
        return TWO_PAIRS, j
    if has_pair(hand)[0]:
        i,j = has_pair(hand)
        return PAIR, j
    return HIGH, highest_card(hand)


def main():
    initialize_random()
    deck = initialize_deck()
    print("Shuffling and dealing...")
    deck, player_hand, computer_hand = shuffle_and_deal(deck)
    print("Press enter to see your hand.")
    input()
    print("Your hand:")
    print_hand(player_hand)


    what_comb, value = check_hand(player_hand)
    print("You have {}, rank card value {}".format(RESULTSTRINGS[what_comb],value))
    change_cards = input("Enter the cards (1-5) you want to change, separated by commas:\n")
    try:
        player_hand = draw_more(deck, player_hand, change_cards)[1]
    except ValueError:
        pass
    print("Your hand:")
    print_hand(player_hand)
    what_comb, value = check_hand(player_hand)
    print("You have {}, rank card value {}".format(RESULTSTRINGS[what_comb], value))
    #print()
    input("Press enter to reveal the computer's hand\n")
    print("Computer hand:")
    print_hand(computer_hand)
    computercomb, computervalue = check_hand(computer_hand)
    print("Computer has {}, rank card value {}".format(RESULTSTRINGS[computercomb], computervalue))
    if computercomb < what_comb:
        print("You won.")
    elif computercomb == what_comb and computervalue < value:
        print("You won.")
    elif computercomb == what_comb and computervalue > value:
        print("Computer won.")
    elif computercomb == what_comb and computervalue == value:
        print("It's a tie.")
    else:
        print("Computer won.")


main()
