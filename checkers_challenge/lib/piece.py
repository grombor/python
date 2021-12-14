class Piece:
    """ A class for pieces. """

    def __init__(self, x, y, color="white", is_king=False):
        self.x = x
        self.y = y
        self.color = color
        self.is_king = is_king
    
    def __str__(self):
        return f"A standard {self.color} checkers piece"

    def move(self):
        return f"moving piece to {self.x}, {self.y}"