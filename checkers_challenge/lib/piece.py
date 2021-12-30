class Piece:
    """ A class for piece object. """

    piece_symbol = ""


    def __init__(self, x=0, y=0, white=False, direction=False, is_king=False, jump=False, active=True, moves=[]):
        self.x = x
        self.y = y
        self.is_white = white               # The color of the piece
        self.is_king = is_king              # If True, it means that the piece reach the king row and become kinged
        self.has_jump = jump                # If True the piece has to jump
        self.move_direction = direction     # need idea here (2-4 directions of movement here) maybe 'L'eft - 'R'ight; 'U'p - 'D'Down
        self.is_active = active             # If True means the piece in game
        self.moves = moves                  # The list with all allowed moves

    
    # function made for easy print of the pieces
    def __str__(self):
        """ Assigns symbols to pieces depend on color (white or not) and status (king of men) """

        global piece_symbol
        if self.is_white: 
            piece_symbol = "\u26c1" if self.is_king else "\u26c2"
        if not self.is_white:
            piece_symbol = "\u26c3" if self.is_king else "\u26c0"
        return piece_symbol

    
    # Moving function prototype
    # Update location of piece
    def move(self, y, x):
        self.x = x
        self.y = y
        

    def draw(self):
        """ Assigns symbols to pieces depend on color (white or not) and status (king or men) """

        global piece_symbol
        if self.is_white: 
            piece_symbol = "\u26c1" if self.is_king else "\u26c0"
        if not self.is_white:
            piece_symbol = "\u26c3" if self.is_king else "\u26c2"
        return print(piece_symbol)


    # Prints list with all possible moves
    def get_moves(self):
        print("moves list here:")
        for move in self.moves:
            print(*move)


    # Sets moves list
    def set_moves(self, move_list):
        self.moves = move_list.copy()
        

