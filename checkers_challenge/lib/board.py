from .piece import Piece

# Checkers board is a list of 8 rows list
board = []


# Generates new game board
def generate_pieces():
    
    # Temporary list of 4 pieces and 4 white fields
    temp = []

    # Generate 1st line of white
    for field in range(1,9,2):
        new_piece = Piece(field, 1, True, "d")
        temp.append(new_piece)
        temp.append("\u2b1c")

    # Add row to the board
    board.append(temp)
    
    # Clear temp
    temp = []


    # Generate 2nd line of white
    for field in range(2,9,2):
        new_piece = Piece(field, 2, True, "d")
        temp.append("\u2b1c")
        temp.append(new_piece)

    # Add row to the board
    board.append(temp)
    
    # Clear temp
    temp = []


    # Generate 3nd line of white
    for field in range(1,9,2):
        new_piece = Piece(field, 3, True, "d")
        temp.append(new_piece)
        temp.append("\u2b1c")

    # Add row to the board
    board.append(temp)
    
    # Clear temp
    temp = []


    # Generate 1st line of empty middle rows
    for field in range(2, 9, 2):
        temp.append("\u2b1c")
        temp.append(" ")

    # Add row to the board
    board.append(temp)
    
    # Clear temp
    temp = []


    # Generate 2nd line of empty middle rows
    for field in range(1, 9, 2):
        temp.append(" ")
        temp.append("\u2b1c")

    # Add row to the board
    board.append(temp)
    
    # Clear temp
    temp = []


    # Generate 1st line of black
    for field in range(2, 9, 2):
        new_piece = Piece(field, 6, False, "u")
        temp.append("\u2b1c")
        temp.append(new_piece)

    # Add row to the board
    board.append(temp)
    
    # Clear temp
    temp = []       


    # Generate 2nd line of black
    for field in range(1, 9, 2):
        new_piece = Piece(field, 7, False, "u")
        temp.append(new_piece)
        temp.append("\u2b1c")

    # Add row to the board
    board.append(temp)
    
    # Clear temp
    temp = []       


    # Generate 3nd line of black
    for field in range(2, 9, 2):
        new_piece = Piece(field, 8, False, "u")
        temp.append("\u2b1c")
        temp.append(new_piece)

    # Add row to the board
    board.append(temp)
    
    # Clear temp
    temp = []       



# Prints board on the screen
def print_board():
    for rows in board:
        print(*rows)


# Generates a board after each turn
def set_board(new_board):
    global board
    board = new_board.copy()

# Loop iterating through all pieces from most distant to the nearest row.
def board_loop(is_white):

    def check_move(piece, move_direction):
        can_move = False
        y = piece.y-1 + move_direction
        x = piece.x-1

        if 0<y<8 and x+1<8 and x-1>0:
            row = board[y]
            if row[x-1] == " ":
                print(f"can place at:{y},{x-1}")
            if row[x+1] == " ":
                print(f"can place at:{y},{x+1}")

        return can_move

    def make_move(piece, move_destination):
        pass

    # Function is iterating piece by piece
    def fields_loop():
        for field in rows:

                # Check if field has piece on it
                if type(field)!= str:

                    # Instructions for white pieces
                    piece = field
                    if piece.is_white:
                        if piece.move_direction == "d":
                            check_move(piece, 1)
                            make_move(piece,0)

                    # Instructions for black pieces
                    if not piece.is_white:
                        if piece.move_direction == "d":
                            print("black  piece, moves up(+1)")
                            print(piece.y, "->", piece.y+1)

                # Instructions for empty field (without piece on it)
                elif field == " ":
                    pass
                    # print("field is empty")

    # Loop for white pieces
    if is_white:
        for rows in reversed(board):
            fields_loop()

    # Loop for black pieces
    elif not is_white:
        for rows in board:
            fields_loop()

