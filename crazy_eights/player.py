from card import Card
from hand import Hand


class Player:

    def __init__(self, name: str):
        self.name = name 
        self.hand = Hand()
        self.points = 0

    def choose_card(self, starter: Card) -> Card | None:
        """
        allows the player to select (via keyboard input) a card to play on the given starter card
        present them with a list of legal options (make use of Hand.search), but also give them the option to play nothing (draw)
        return the selected Card object, or return None if no legal plays are possible or the player chooses to draw.
        """
        
        legal_plays = self.hand.search(starter)
        print(legal_plays)

        play = input(f'Choose a card to play, or write "None" to skip.')

        if play == "None":
            return None
        
        return legal_plays[int(play)]

            

       
        

