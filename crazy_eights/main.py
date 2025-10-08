from game import CrazyEightsGame

g = CrazyEightsGame()

# 2 player game, so call add_player twice
g.add_player()
g.add_player()

# run a round of the game
g.play_round()
