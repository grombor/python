class Piece:
    """ A class for piece object. """

    piece_symbol = ""


    def __init__(self, x, y, white=False, is_king=False, jump=False, direction=False, active=True):
        self.x = x                          # The X position of the piece on the board
        self.y = y                          # The Y position of the piece on the board
        self.is_white = white               # The color of the piece
        self.is_king = is_king              # If True, it means that the piece reach the king row and become kinged
        self.has_jump = jump                # If True the piece has to jump
        self.move_direction = direction     # need idea here (2-4 directions of movement here) maybe 'L'eft - 'R'ight; 'U'p - 'D'Down
        self.is_active = active             # If True means the piece in game

    
    # function made for debugging only
    def __str__(self):
        return f"This piece is:\nat position x: {self.x} y: {self.y}\nwhite color: {self.is_white}\nkinged: {self.is_king}\nhas to jump:{self.has_jump}\nmoving direction: {self.move_direction}\nin game: {self.is_active}"

    
    # Moving function prototype
    def move(self, x, y):
        return print(f"moving piece to {x}, {y}")

    
    def symbol(self):
        global piece_symbol
        if self.is_white: 
            if not self.is_king:
                piece_symbol = "\u26c0"
            else:
                piece_symbol = "\u26c1"
        if not self.is_white:
            if not self.is_king:
                piece_symbol = "\u26c2"
            else:
                piece_symbol = "\u26c3"
        return piece_symbol
        

