class Node:
  def __init__(self, state, player):
    self.state = state
    self.player = player
    self.winner = None
    self.children = []
  
  def print_state(self):
    for i in range(len(self.state)):
      row = self.state[i]
      row_string = ''
      for space in row:
        if space == None:
          row_string += '_|'
        else:
          row_string += space + '|'
      print(row_string[:-1])
    print('\n')

class GameTree:
  def __init__(self, first):
    self.root = Node([[None for _ in range(3)] for _ in range(3)], first)
    self.node_num = 0
    self.leaf_node_num = 0

  def get_open_spaces(self, state):
    open_spaces = [(i,j) for i in range(3) for j in range(3) if state[i][j] == None]
    return open_spaces

  def get_opposite_symbol(self, symbol):
    if symbol == 'X':
      return 'O'
    elif symbol == 'O':
      return 'X'
  
  def check_for_winner(self, state):
    rows = state.copy()
    cols = [[state[i][j] for i in range(3)] for j in range(3)]
    diags = [[state[i][i] for i in range(3)],
             [state[i][2-i] for i in range(3)]]

    board_full = True
    for row in (rows + cols + diags):
      if None in row:
        board_full = False

      for symbol in ['X','O']:
        if row == [symbol for _ in range(3)]:
          return symbol
    
    if board_full:
      return 'Tie'
    return None

  def build_tree(self, node):
    for space in self.get_open_spaces(node.state):
      new_state = [[node.state[i][j] for j in range(3)] for i in range(3)]
      new_state[space[0]][space[1]] = node.player
      new_node = Node(new_state, self.get_opposite_symbol(node.player))
      new_node.winner = self.check_for_winner(new_state)
      node.children.append(new_node)
      self.node_num += 1
      if new_node.winner == None:
        self.build_tree(new_node)
      else:
        self.leaf_node_num += 1
