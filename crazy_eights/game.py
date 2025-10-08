from crazy_eights import player
l=[['a',10],['b',12],[',c',15]]
for i in l:
    pass
class CrazyEightsGame:

    def __init__(self):
        self.player_List=[]
        
    def add_player(self):
        """
        Ask a player to enter (at the keyboard) their name
        Create a Player object for them, and add it to the list of players for this game
        """
        name=str(input("enter your name"))
        player=Player(name,0)
        self.playerList.append(player)
        # your code here

    def play_round(self,deck):
        """
        play one round of crazy eights
        Reset/shuffle the deck and deal each player their starting hand.
        At each player's turn, ask them to choose from the possible cards to play, or deal them new cards as appropriate
        (make use of Hand.search and Player.choose_card)
        When a player wins the round, update their score
        """
        deck.reset()
        deck.shuffle()
        for player in self.player_List:
            for i in range(5):
                player.hand.add(deck.deal())
            top_card=deck.deal()
        playing=True
        while playing:
            for i in self.player_List[0:1]:
                potential_cards=player.hand.search()
                while len(potential_cards) == 0:
                    try:
                        player.deck.deal()
                        potential_cards=player.hand.search()
                    except:
                        print("no cards left")
                player.choose_card(potential_cards)
    
        pass # your code here