import sys
from tic_tac_toe import *
from game_tree import *
sys.path.append('games-cohort-2/tic-tac-toe/players')
from random_player import *


game = GameTree(1)
game.contruct_tree()
print(game.leaf_nodes, 'leaf nodes')
