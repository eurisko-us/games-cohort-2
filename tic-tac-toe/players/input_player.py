class InputPlayer():
    
    def __init__(self):
        self.player_number = None

    def set_player_symbol(self, n):
        self.symbol = n
  
    def set_player_number(self, n):
        self.number = n

    def choose_move(self, choices):
        
        move = None

        while not self.is_move_valid(move, choices):
            
            if move == None:
                move = input("\nYour move: ")
            else:
                print("that move is not valid")
                move = input("Your move: ")
                    
        return self.format_move(move)

    def format_move(self, move):
        
        for char in move:
            if char in ', ':
                move = move.replace(char, '')
        
        return tuple([int(elem) for elem in move][::-1])

    def is_move_valid(self, move, choices):

        if move == None:
            return False
        
        for elem in move:
            if elem not in '012, ':
                return False

        if ',' not in move:
            return False

        move = self.format_move(move)

        if len(move) != 2:
            return False

        if move not in choices:
            return False
        
        return True