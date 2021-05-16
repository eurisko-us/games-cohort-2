import sys
sys.path.append('games-cohort-2/tic-tac-toe')
from game_tree import *

class MinimaxPlayer():
    def __init__(self):
        self.player_num = None
    
    def set_player_number(self, player_num):
        self.player_num = player_num
    
    def choose_move(self, game_state):
        game = GameTree(game_state, self.player_num)
        game.create_game_tree()
        game.set_node_scores()
        return game.get_best_move()