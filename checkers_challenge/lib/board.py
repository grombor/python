from .piece import Piece

# Checkers board is a list of 8 rows list
board = []


# Generates new game board
def generate_pieces():
    
    # Temporary list of 4 pieces and 4 white fields
    temp = []

    # Generate 1st line of white
    for field in range(0,8,2):
        new_piece = Piece(field, 0, True, "d")
        temp.append(new_piece)
        temp.append("\u2b1c")

    # Add row to the board
    board.append(temp)
    
    # Clear temp
    temp = []


    # Generate 2nd line of white
    for field in range(1,8,2):
        new_piece = Piece(field, 1, True, "d")
        temp.append("\u2b1c")
        temp.append(new_piece)

    # Add row to the board
    board.append(temp)
    
    # Clear temp
    temp = []


    # Generate 3nd line of white
    for field in range(0,8,2):
        new_piece = Piece(field, 2, True, "d")
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
    for field in range(1, 9, 2):
        new_piece = Piece(field, 5, False, "u")
        temp.append("\u2b1c")
        temp.append(new_piece)

    # Add row to the board
    board.append(temp)
    
    # Clear temp
    temp = []       


    # Generate 2nd line of black
    for field in range(0, 8, 2):
        new_piece = Piece(field, 6, False, "u")
        temp.append(new_piece)
        temp.append("\u2b1c")

    # Add row to the board
    board.append(temp)
    
    # Clear temp
    temp = []       


    # Generate 3nd line of black
    for field in range(1, 9, 2):
        new_piece = Piece(field, 7, False, "u")
        temp.append("\u2b1c")
        temp.append(new_piece)

    # Add row to the board
    board.append(temp)
    
    # Clear temp
    temp = []


def piece_move(piece, y, x):
    
    # Put piece at the new position
    board[y][x] = piece
    
    # Remove piece from old position
    piece_previous_x = piece.x
    piece_previous_y = piece.y
    board[piece_previous_y][piece_previous_x] = " "
    
    # Set new x and y for piece
    piece.x = x
    piece.y = y
    



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
    move_destination = []

    # Checks all possible moves for piece
    def check_move(piece, move_direction):
        can_move = False
        move_priority = 0
        next_move = []
        y = piece.y-1 + move_direction
        x = piece.x-1

        # Checking is next field is available to move on
        if 0<y<8 and x+1<8 and x-1>0:

            # Go to next row
            row = board[y]

            # Check is next field is empty
            if row[x-1] == " ":     # this statement should be refactored to function
                print(f"can place at:{y},{x-1}")
                can_move = True
                move_priority = 1
                next_move.append([move_priority, y, x-1])

            # Check is next field is empty
            if row[x+1] == " ":     # this statement should be refactored to function
                print(f"can place at:{y},{x+1}")
                can_move = True
                move_priority = 1
                next_move.append([move_priority, y, x+1])

            # If piece has to jump opportunity
            next_row = board[y+1]
            if 0<x-2<8 and 0<x+2<8:

                # If next row diagonal fieldsare on the board
                if row[x-1] != " " and next_row[x-2] == " ":
                    # if piece in next row is not the same color do:
                    if not (row[x-1].is_white and is_white):
                        print("jump")
                        can_move = True
                        move_priority = 2
                        next_move.clear()                   # <==== Check if has any high priority move on the list, if no then clear the list
                        next_move.append([move_priority, y, x-2])

                # If next row diagonal fieldsare on the board
                if row[x+1] != " " and next_row[x+2] == " ":
                    # if piece in next row is not the same color do:
                    if not (row[x-1].is_white and is_white):
                        print("jump")
                        can_move = True
                        move_priority = 2
                        next_move.clear()                   # <==== Check if has any high priority move on the list, if no then clear the list
                        next_move.append([move_priority, y, x+2])

        
        # Returns possible moves list
        return next_move

    def make_move(piece, move_destination):
        # Takes piece and move_destination to move the piece to new position, affter that ends turn
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
                            piece.set_moves(check_move(piece, 1))
                            make_move(piece,0)

                    # Instructions for black pieces
                    if not piece.is_white:
                        if piece.move_direction == "d":
                            piece.set_moves(check_move(piece, 1))
                            make_move(piece,0)
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

