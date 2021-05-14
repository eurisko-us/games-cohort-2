import copy

class Node():
    def __init__(self, state, player_turn):
        self.state = state
        self.player_turn = player_turn
        self.winner = None
        self.children = None

    def check_for_winner(self):
        rows = self.state.copy()
        cols =  [[self.state[i][j] for i in range(3)] for j in range(3)]
        diags = [[self.state[i][i] for i in range(3)],
                 [self.state[i][2-i] for i in range(3)]]

        board_full = True
        for row in rows + cols + diags:
            if None in row:
                board_full = False

            for player in [1, 2]:
                if row == [player for _ in range(3)]:
                    return player
        
        if board_full:
            return 'Tie'
        return None

class Tree():

    def __init__(self, empty_board, player_number):
        self.root = Node(empty_board, player_number)
        self.num_leaf_nodes = 0

    def other_player(self, node):
        return 1 if node.player_turn == 2 else 2

    def build_tree(self):
        
        self.make_children(self.root)
        children = self.root.children
        while len(children) != 0:
            children = self.get_grandchildren(children)

    def get_grandchildren(self, children):
        
        grandchildren = []
        for child in children:
            
            winner = child.check_for_winner()
            if winner is None:
                
                self.make_children(child)
                for grandchild in child.children:
                    grandchildren.append(grandchild)
            
            else:
                child.winner = winner
                self.num_leaf_nodes += 1

        return grandchildren

    def make_children(self, node):
        
        children = []
        for row_index in range(3):
            for col_index in range(3):
        
                if node.state[row_index][col_index] is None:
                   
                    child_board = copy.deepcopy(node.state)
                    child_board[row_index][col_index] = self.other_player(node)
                    child_node = Node(child_board, self.other_player(node))
                    children.append(child_node)
        
        node.children = children

empty_board = [[None for _ in range(3)] for _ in range(3)]
tree = Tree(empty_board, 1)
tree.build_tree()
print(tree.num_leaf_nodes)