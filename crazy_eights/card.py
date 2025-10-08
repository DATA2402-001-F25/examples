
class Card:

    def __init__(self, rank: int, suit: str):
        self.rank = rank 
        self.suit= suit 
        
        # pass # your code here

    def get_point_value(self) -> int:
        """
        return the point value for this card
        """
        if self.rank in [11, 12, 13] or self.rank in ["K", "J", "Q"]:
            return 10
        elif self.rank == 1 or self.rank == "A":
            return 11
        elif self.rank == 8:
            return 50
        else:
            return self.rank
             

        
        # pass # your code here

    def __repr__(self) -> str:
        """
        return a human-readable string representation of the card
        """
        # pass # your code here
        return (f"{self.rank} of {self.suit}")
    