import enum
import random


class Value(enum.Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


class Suit(enum.Enum):
    DIAMONDS = 1
    CLUBS = 2
    HEARTS = 3
    SPADES = 4


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return '{} of {}'.format(
            self.value.name.capitalize(),
            self.suit.name.capitalize())

    def __repr__(self):
        return self.__str__()


class Deck:
    def __init__(self):
        self.counter = -1
        self.__deck = self.__init_deck()

    def __init_deck(self):
        deck = []

        for suit in Suit:
            for value in Value:
                deck.append(Card(value, suit))

        return deck

    def shuffle(self):
        random.shuffle(self.__deck)

    def get_card(self):
        self.counter += 1
        if self.counter > len(self.__deck):
            raise IndexError('DECK IS EMPTY!')
        return self.__deck[self.counter]


deck = Deck()
deck.shuffle()
try:
    while True:
        print(deck.get_card())
except IndexError:
    print('STOP!')
