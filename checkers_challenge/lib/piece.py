class Piece:
    """ A class for piece object. """

    piece_symbol = ""


    def __init__(self, x=0, y=0, white=False, is_king=False):
        self.x = x
        self.y = y
        self.is_white = white               # The color of the piece
        self.is_king = is_king              # If True, it means that the piece reach the king row and become kinged

    
    # function made for easy print of the pieces
    def __str__(self):
        """ Assigns symbols to pieces depend on color (white or not) and status (king of men) """

        global piece_symbol
        if self.is_white: 
            piece_symbol = "\u26c3" if self.is_king else "\u26c2"
        if not self.is_white:
            piece_symbol = "\u26c1" if self.is_king else "\u26c0"
        return piece_symbol

    
    # Update location of piece
    def set_yx(self, y, x):
        self.x = x
        self.y = y


    # Prints list with all possible moves
    def get_xy(self):
        return [self.x, self.y]


    # Sets moves list
    def set_moves(self, move_list):
        self.moves = move_list.copy()

    # Sets piece to king
    def set_king(self):
        global piece_symbol
        if self.is_white:
            self.is_king = True
            piece_symbol = "\u26c3"
        elif not self.is_white:
            self.is_king = True
            piece_symbol = "\u26c1"
        