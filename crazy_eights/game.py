from player import Player
from deck import Deck


class CrazyEightsGame:

    def __init__(self):
        self.player_List=[]
        
    def add_player(self):
        """
        Ask a player to enter (at the keyboard) their name
        Create a Player object for them, and add it to the list of players for this game
        """
        name=str(input("enter your name"))
        player=Player(name)
        self.player_List.append(player)

    def play_round(self):
        """
        play one round of crazy eights
        Reset/shuffle the deck and deal each player their starting hand.
        At each player's turn, ask them to choose from the possible cards to play, or deal them new cards as appropriate
        (make use of Hand.search and Player.choose_card)
        When a player wins the round, update their score
        """
        deck = Deck()
        deck.reset()

        for player in self.player_List:
            for i in range(5):
                player.hand.add(deck.deal())
        
        top_card=deck.deal()
        
        playing=True
        while playing:
            for player in self.player_List:
                print(f"{player.name}'s turn")
                print(f"top card is {top_card}")

                print(f"your hand: {player.hand}")
                choice = player.choose_card(top_card)

                if choice is None:
                    player.hand.add(deck.deal())
                    print(f'your new hand is {player.hand}')
                else:
                    top_card = choice
                
                # check for game end
                if player.hand.is_empty():
                    playing = False
        
        # scoring logic here
        

