import sys
from tic_tac_toe import *
sys.path.append('tic-tac-toe/players')
from random_player import *
from minimax_player import *
'''
players = [RandomPlayer(), RandomPlayer()]
game = TicTacToe(players)

game.print_board()

game.complete_round()
game.print_board()

game.run_to_completion()
game.print_board()
print(game.round)
print(game.winner)

num_wins = {1: 0, 2: 0, 'Tie':0}

for _ in range(1000):
  players = [RandomPlayer(), RandomPlayer()]
  game = TicTacToe(players)
  game.run_to_completion()
  winner = game.winner

  num_wins[winner] += 1
print(num_wins)
'''
alternate = False
players = [MinimaxPlayer(), RandomPlayer()]
tracker = ['minimax', 'random']
wins = {'minimax': 0, 'random': 0, 'tie': 0}
for i in range(1,8):
    if alternate:
        players = players[::-1]
        tracker = tracker[::-1]
    game = TicTacToe(players)
    game.run_to_completion()
    print("winner: ",end="")
    if game.winner == 'Tie':
        wins['tie'] += 1
        print("tie")
    else:
        wins[tracker[game.winner - 1]] += 1
        print(str(tracker[game.winner - 1]))
    alternate = not alternate
print(wins)