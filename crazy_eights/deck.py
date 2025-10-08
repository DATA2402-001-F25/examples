from card import Card
import random

class Deck:

    def __init__(self):

        self.cards = list()
        pass # your code here

    def shuffle(self) -> list:
        """
        randomize the order of the cards in the deck
        (check out random.shuffle: https://www.w3schools.com/python/ref_random_shuffle.asp)
        """

        random.shuffle(self.cards)
        return self.cards
        pass # your code here

    def reset(self) -> list:
        """
        fill the deck will the 52 standard cards (ranks 1-13 for each of 4 suits)
        then shuffle it
        """
        HEART = 13
        CLUBS = 13
        DIAMONDS = 13
        SPADE = 13
        i=1
        while i <= SPADE:
            self.cards.append(Card(rank=i, suit="spades"))
            i+=1

        i=1
        while i <= HEART:
            self.cards.append(Card(rank=i, suit="hearts"))
            i+=1

        i=1
        while i <= CLUBS:
            self.cards.append(Card(rank = i, suit="clubs"))
            i+=1

        i=1
        while i <= DIAMONDS:
            self.cards.append(Card(rank=i, suit="diamonds"))
            i+=1

        self.shuffle()
        return self.cards
        pass # your code here

    def deal(self) -> Card:
        """
        remove and the return the first card from the deck
        raise an exception if the deck is empty
        """
        if len(self.cards) < 1:
            raise ValueError("Deck is empty")

        first_card = self.cards[0]

        self.cards.remove(first_card)
        return first_card
        pass # your code here

deck = Deck()
deck.reset()
deck.deal()

