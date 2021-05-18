import copy

class Node():
    def __init__(self, state, turn, player):
        self.state = state
        self.turn = turn
        self.player = player
        self.prev = None
        self.children = None
        self.winner = self.check_for_winner()
        self.score = None
        self.coord = None 
    
    def get_rows_cols_diags(self):
        rows = list(self.state)
        cols = [[self.state[i][j] for i in range(3)] for j in range(3)]
        diag_1 = [self.state[i][i] for i in range(3)]
        diag_2 = [self.state[i][2-i] for i in range(3)]
        diags = [diag_1, diag_2]
        return rows + cols + diags
    
    def check_for_winner(self):
        rows_cols_diags = self.get_rows_cols_diags()
        valid_rcd = [item for item in rows_cols_diags if None not in item]
        for item in valid_rcd:
            if len(set(item)) == 1:
                return item[0]
        if valid_rcd == rows_cols_diags:
            return "Tie"
        return None
    
    def children_to_score(self):
        if self.children == None:
            return None
        for child in self.children:
            child.set_score()
        return [child.score for child in self.children]
    
    def set_score(self):
        if self.children == None:
            if self.winner == self.player:
                self.score = 1
            elif self.winner == 3 - self.player:
                self.score = -1
            elif self.winner == 'Tie':
                self.score = 0
            return

        if self.turn == self.player:
            self.score = max(self.children_to_score())
        elif self.turn == 3 - self.player:
            self.score = min(self.children_to_score())

class GameTree():
    def __init__(self, root_state, player_num):
        self.root = Node(root_state, 1, player_num)
        self.player = player_num
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
            child = Node(board_copy, 3-turn, self.player)
            child.coord = option
            child.prev = node
            children.append(child)
        node.children = children

    def create_game_tree(self):
        if len(self.current_nodes) == 0:
            self.current_nodes = [self.root]
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
    
    def set_node_scores(self):
        assert self.root.children != None, "create game tree before setting scores"
        self.root.set_score()
        return
    
    def get_best_move(self):
        scores = [node.score for node in self.root.children]
        max_index = scores.index(max(scores))
        best_result = self.root.children[max_index]
        return best_result.coord
