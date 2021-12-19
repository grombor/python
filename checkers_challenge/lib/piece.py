class Piece:
    """ A class for piece object. """

    piece_symbol = ""


    def __init__(self, x=0, y=0, white=False, is_king=False, jump=False, direction=False, active=True):
        self.x = x
        self.y = y
        self.is_white = white               # The color of the piece
        self.is_king = is_king              # If True, it means that the piece reach the king row and become kinged
        self.has_jump = jump                # If True the piece has to jump
        self.move_direction = direction     # need idea here (2-4 directions of movement here) maybe 'L'eft - 'R'ight; 'U'p - 'D'Down
        self.is_active = active             # If True means the piece in game

    
    # function made for debugging only
    def __str__(self):
        """ Assigns symbols to pieces depend on color (white or not) and status (king of men) """

        global piece_symbol
        if self.is_white: 
            # if not self.is_king:
            #     piece_symbol = "\u26c0"
            # else:
            #     piece_symbol = "\u26c1"
            piece_symbol = "\u26c1" if self.is_king else "\u26c2"
        if not self.is_white:
            # if not self.is_king:
            #     piece_symbol = "\u26c2"
            # else:
            #     piece_symbol = "\u26c3"
            piece_symbol = "\u26c3" if self.is_king else "\u26c0"
        return piece_symbol

    
    # Moving function prototype
    def move(self, x, y):
        return print(f"moving piece to {x}, {y}")

    
    def draw(self):
        """ Assigns symbols to pieces depend on color (white or not) and status (king of men) """

        global piece_symbol
        if self.is_white: 
            # if not self.is_king:
            #     piece_symbol = "\u26c0"
            # else:
            #     piece_symbol = "\u26c1"
            piece_symbol = "\u26c1" if self.is_king else "\u26c0"
        if not self.is_white:
            # if not self.is_king:
            #     piece_symbol = "\u26c2"
            # else:
            #     piece_symbol = "\u26c3"
            piece_symbol = "\u26c3" if self.is_king else "\u26c2"
        return print(piece_symbol)
        

