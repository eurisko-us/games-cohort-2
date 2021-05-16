from random import random
import math

class RandomPlayer:
  def __init__(self):
    self.symbol = None
    self.player_num = None
  
  def set_player_symbol(self, n):
    self.symbol = n
  
  def set_player_number(self, n):
    self.player_num = n
  
  def choose_move(self, game_state):
    choices = [(i,j) for i in range(len(game_state)) for j in range(len(game_state)) if game_state[i][j]==None]
    random_idx = math.floor(len(choices) * random())
    return choices[random_idx]
