import copy

class Node():
  def __init__(self, state, player):
    self.state = state
    self.player = player
    self.winner = None
    self.children = None
  
  def check_for_winner(self):
    rows = self.state.copy()
    cols = [[self.state[i][j] for i in range(3)] for j in range(3)]
    diags = [[self.state[i][i] for i in range(3)],
             [self.state[i][2-i] for i in range(3)]]

    board_full = True
    for row in rows + cols + diags:
      if None in row:
        board_full = False

      for player in [1,2]:
        if row == [player for _ in range(3)]:
          return player
    
    if board_full:
      return 'Tie'
    return None

class GameTree():
  def __init__(self, starting_player):
    self.root = Node([[None for _ in range(3)] for _ in range(3)], starting_player)
    self.leaf_nodes = 0


  def contruct_tree(self):
    self.set_children(self.root)
    current_layer = self.root.children
    while len(current_layer) != 0:
      next_layer = self.get_next_layer(current_layer)
      current_layer = next_layer

  def get_next_layer(self, layer):
    new_layer = []
    for child in layer:
      winner = child.check_for_winner()
      if winner is None:
        self.set_children(child)
        for sub_child in child.children:
          new_layer.append(sub_child)
      else:
        child.winner = winner
        self.leaf_nodes += 1

    return new_layer

  def set_children(self, parent):
    children = []
    for row_index in range(len(parent.state)):
      for column_index in range(len(parent.state[row_index])):
        if parent.state[row_index][column_index] is None:
          child = copy.deepcopy(parent.state)
          child[row_index][column_index] = self.opposite_player(parent.player)
          children.append(Node(child, self.opposite_player(parent.player)))
    parent.children = children


  def opposite_player(self, player):
    if player == None:
      return None
    elif player == 1:
      return 2
    elif player == 2:
      return 1