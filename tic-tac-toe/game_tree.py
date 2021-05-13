import copy

class GameNode():
    def __init__(self, game_state, player_turn):
        self.state = game_state
        self.turn = player_turn
        self.winner = self.check_for_winner()
        self.previous = None
        self.children = None
    
    def get_row_col_diag(self):
        rows = list(self.state)
        cols = [[self.state[i][j] for i in range(3)] for j in range(3)]
        diag_1 = [self.state[i][i] for i in range(3)]
        diag_2 = [self.state[i][2-i] for i in range(3)]
        diags = [diag_1, diag_2]
        return rows + cols + diags
    
    def check_for_winner(self):
        rcd = self.get_row_col_diag()
        valid_rcd = [item for item in rcd if None not in item]
        for item in valid_rcd:
            if len(set(item)) == 1:
                return item[0]
        if valid_rcd == rcd:
            return "Tie"
        return None

class GameTree():
    def __init__(self, root_state):
        self.root = GameNode(root_state, 1)
        self.current_nodes = [self.root] # for creating the game tree
        self.tree_len = 1
        self.terminal_nodes = 0
    
    def create_node_children(self, node):
        if node.winner != None or node.children != None:
            return
        board = node.state
        turn = node.turn
        children = []
        options = [(i,j) for i in range(len(board)) for j in range(len(board)) if board[i][j] == None]
        for option in options:
            board_copy = copy.deepcopy(board)
            board_copy[option[0]][option[1]] = turn
            child = GameNode(board_copy, 3-turn)
            child.previous = node
            children.append(child)
        node.children = children

    def create_game_tree(self):
        if len(self.current_nodes) == 0:
            return
        all_children = []
        for node in self.current_nodes:
            self.create_node_children(node)
            if node.children != None:
                all_children += node.children
                self.tree_len += len(node.children)
            else:
                self.terminal_nodes += 1
        self.current_nodes = all_children
        self.create_game_tree()
        

root_state = [[None, None, None],[None, None, None],[None, None, None]]
game = GameTree(root_state)
game.create_game_tree()
print(game.tree_len)
print(game.terminal_nodes)
