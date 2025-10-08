from card import Card


class Hand:

    def __init__(self):
        self.cards = []

    def add(self, card: Card):
        """
        add a card to the hand
        """
        self.cards.append(card)
    
    def remove(self, card: Card):
        """
        remove the specified card from the hand
        """
        self.cards.remove(card)

    def score(self) -> int:
        """
        return the point total for this hand
        """
        return sum([i.get_point_value() for i in self.cards])

    def search(self, starter: Card) -> list[Card]:
        """
        find cards in this hand that could be played on the given starter Card
        return a list of playable cards
        """
        playable = []
        for card in self.cards:
            if card.rank == 8:
                playable.append(card)
            elif card.rank == starter.rank:
                playable.append(card)
            elif card.suit == starter.suit:
                playable.append(card)
        return playable

    def is_empty() -> bool:
        return len(self.cards) == 0

    def __repr__(self) -> str:
        """
        return a human-readable string representation of the cards in the hand
        """
        s = "Hand containing "
        i = "" 
        for card in self.cards:
            i += str(card)
            i += ", "
        i = i[:-2]
        return s + i
    

