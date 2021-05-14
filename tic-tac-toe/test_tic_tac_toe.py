import sys
from tic_tac_toe import *
sys.path.append('games-cohort-2/tic-tac-toe/players')
from random_player import *
from input_player import *

game_options = ['random vs random', 'player vs random', 'random vs player', 'player vs player']
game_type = game_options[3] # choose here
players = [RandomPlayer() if elem == 'random' else InputPlayer() for elem in game_type.split(' vs ')]

if game_type == 'random vs random':

    game = TicTacToe(players, second_player_first=False)
    game.print_board()
    game.complete_round()
    game.print_board()
    game.run_to_completion()
    game.print_board()
    
    print("\ngame.round:", game.round)
    print("game.winner:", game.winnerm, '\n')

    num_wins = {1: 0, 2: 0, 'Tie':0}

    for i in range(1000):
        players = [RandomPlayer(), RandomPlayer()]
        game = TicTacToe(players, second_player_first = (i % 2 == 1))
        game.run_to_completion()
        num_wins[game.winner] += 1

    print(num_wins)

else:

    game = TicTacToe(players, second_player_first=False, see_board=True)
    game.run_to_completion()
    game.print_board()
    print("\nwinner:", game.winner)