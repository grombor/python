from .piece import Piece

# Checkers board is a list of 8 rows list
board = []

def generate_pieces():
    
    # Temporary list of 4 pieces and 4 white fields
    temp = []

    # Generate 1st line of white
    for field in range(1,9,2):
        new_piece = Piece(field,1,True)
        temp.append(new_piece)
        temp.append("\u2b1c")

    board.append(temp)
    temp = []

    # Generate 2nd line of white
    for field in range(2,9,2):
        new_piece = Piece(field,2,True)
        temp.append("\u2b1c")
        temp.append(new_piece)

    board.append(temp)
    temp = []

    # Generate 3nd line of white
    for field in range(1,9,2):
        new_piece = Piece(field,3,True)
        temp.append(new_piece)
        temp.append("\u2b1c")

    board.append(temp)
    temp = []

    # Generate 1st line of empty middle rows
    for field in range(2,9,2):
        temp.append("\u2b1c")
        temp.append(" ")

    board.append(temp)
    temp = []

    # Generate 2nd line of empty middle rows
    for field in range(1,9,2):
        temp.append(" ")
        temp.append("\u2b1c")

    board.append(temp)
    temp = []

    # Generate 1st line of black
    for field in range(2,9,2):
        new_piece = Piece(field,6,False)
        temp.append("\u2b1c")
        temp.append(new_piece)

    board.append(temp)
    temp = []       

    # Generate 2nd line of black
    for field in range(1,9,2):
        new_piece = Piece(field,7,False)
        temp.append(new_piece)
        temp.append("\u2b1c")

    board.append(temp)
    temp = []       

    # Generate 3nd line of black
    for field in range(2,9,2):
        new_piece = Piece(field,8,False)
        temp.append("\u2b1c")
        temp.append(new_piece)

    board.append(temp)
    temp = []       


def print_board():
    for rows in board:
        print(*rows)