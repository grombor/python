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
# if is_white = True => means its white turn
def board_loop(is_white):
        
    all_possible_moves = []

    # Checks all possible moves for piece, return list where sublist is [priority, y, x]
    # move_direction = 1 --> move down
    # move direction = -1 --> move up
    def check_move(piece, move_direction):
        move_priority = None
        y = piece.y + move_direction
        x = piece.x
        next_move = []


        # Checking is next field is available to move on
        if 0<y<8:

            # Go to next row
            row = board[y]

            # Check is next field is empty
            if (x-1>=0) and row[x-1] == " ":     # this statement should be refactored to function
                move_priority = 1
                next_move.append([move_priority, y, x-1])

            # Check is next field is empty
            if (x+1<8) and row[x+1] == " ":     # this statement should be refactored to function
                move_priority = 1
                next_move.append([move_priority, y, x+1])


            # If piece has to jump opportunity --> need testing
            if y+1<8:
                next_row = board[y+1]

            # JUMPS HERE ---> need testing

            # If next row diagonal fieldsare on the board
            # if row[x-1] != " " and next_row[x-2] == " ":
            #     # if piece in next row is not the same color do:
            #     if not (row[x-1].is_white and is_white):
            #         print("jump")
            #         move_priority = 2
            #         next_move.clear()                   # <==== Check if has any high priority move on the list, if no then clear the list
            #         next_move.append([move_priority, y, x-2])

            # # If next row diagonal fieldsare on the board
            # if row[x+1] != " " and next_row[x+2] == " ":
            #     # if piece in next row is not the same color do:
            #     if not (row[x-1].is_white and is_white):
            #         print("jump")
            #         move_priority = 2
            #         next_move.clear()                   # <==== Check if has any high priority move on the list, if no then clear the list
            #         next_move.append([move_priority, y, x+2])

        # Returns possible moves list
        return next_move

    def make_move(piece, move_list):

        # If piece has move
        if len(move_list)>0:
            # Add move to global moves list
            for move in move_list:
                new_move = [move, piece]
                all_possible_moves.append(new_move)
                print(f"all_possible_moves list: {all_possible_moves}")
        # sort list by priority now
        # pick first from all_possible_moves as choosen move    

    # Function is iterating piece by piece
    def fields_loop():
        for field in rows:

                # Check if field has piece on it
                if type(field)!= str:

                    # Instructions for white pieces
                    piece = field

                    if piece.is_white:

                        # ckeck all possible moves
                        print(f"checkin moves for piece: {piece.y}:{piece.x}")
                        check_move(piece, 1)
                        if len(check_move(piece, 1))>0:
                            print(f"possible move(s): {check_move(piece, 1)}")
                            make_move(piece, check_move(piece,1))
                        

                    # Instructions for black pieces, still TODO
                    if not piece.is_white:
                        # if piece.move_direction == "d":
                        #     piece.set_moves(check_move(piece, 1))
                        #     make_move(piece,0)
                        #     print("black  piece, moves up(+1)")
                        #     print(piece.y, "->", piece.y+1)
                        pass

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

