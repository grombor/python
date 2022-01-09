from .piece import Piece
from random import randrange
from loguru import logger as log

"""
Checkers board is a list of 8 rows list
0 [fields from 0..7]
1 [fields from 0..7]
2 [fields from 0..7]
3 [fields from 0..7]
4 [fields from 0..7]
5 [fields from 0..7]
6 [fields from 0..7]
7 [fields from 0..7]
Top row belong to white pieces, down ones for black pieces.
"""

board = []


# Generates new game board
def generate_pieces():
    
    # Temporary list of 4 pieces and 4 white fields
    temp = []

    # Generate 1st line of white
    for field in range(0,8,2):
        new_piece = Piece(field, 0, True)
        temp.append(new_piece)
        temp.append("\u2b1c")

    # Add row to the board
    board.append(temp)
    
    # Clear temp
    temp = []


    # Generate 2nd line of white
    for field in range(1,8,2):
        new_piece = Piece(field, 1, True)
        temp.append("\u2b1c")
        temp.append(new_piece)

    # Add row to the board
    board.append(temp)
    
    # Clear temp
    temp = []


    # Generate 3nd line of white
    for field in range(0,8,2):
        new_piece = Piece(field, 2, True)
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
        new_piece = Piece(field, 5, False)
        temp.append("\u2b1c")
        temp.append(new_piece)

    # Add row to the board
    board.append(temp)
    
    # Clear temp
    temp = []       


    # Generate 2nd line of black
    for field in range(0, 8, 2):
        new_piece = Piece(field, 6, False)
        temp.append(new_piece)
        temp.append("\u2b1c")

    # Add row to the board
    board.append(temp)
    
    # Clear temp
    temp = []       


    # Generate 3nd line of black
    for field in range(1, 9, 2):
        new_piece = Piece(field, 7, False)
        temp.append("\u2b1c")
        temp.append(new_piece)

    # Add row to the board
    board.append(temp)
    
    # Clear temp
    temp = []

# Check is jump possible
def check_jump(piece, move_direction):
    y = piece.y
    x = piece.x
    has_jump = []

    # Check is jump possible
    if y + 2*move_direction in range (8):
    
        # Check the next row diagonaly
        left = x-1      # field diagonally on the left
        right = x+1     # field diagonally on the right

        # If it is a field on the left of current piece
        if left in range(8):

            # Go check next row, check field on the diagonal left
            field = board[y+move_direction][x-1]

            # Check is there a piece and
            # Check is the different color than current piece
            if type(field) == Piece and field.is_white != piece.is_white:

                # Go to next row, check is a free field here
                new_y = y+2*move_direction
                new_x = left-1
                if (new_y in range(8)) and new_x in range(8):
                    next_field = board[new_y][new_x]

                    # Check if field in on the board
                    if type(next_field) == str and (y in range(8)) and (x in range(8)):
                        
                        if next_field == " ":
                            has_jump.append([2,new_y,new_x])
                            
                            #Remove jumped piece from the board
                            board[field.y][field.x] = " "
                            set_board(board)

                            temp_piece = Piece(new_x, new_y, piece.is_white)
                            temp = check_jump(temp_piece, move_direction)
                            if len(temp)>0:
                                return temp



        if right in range(8):

            # Go check next row, check field on the diagonal left
            field = board[y+move_direction][x+1]

            # Check is there a piece and
            # Check is the different color than current piece
            if type(field) == Piece and field.is_white != piece.is_white:

                # Go to next row, check is a free field here
                new_y = y+2*move_direction
                new_x = right+1
                if (new_y in range(8)) and new_x in range(8):
                    next_field = board[new_y][new_x]

                    # Check if field in on the board
                    if type(next_field) == str and (y in range(8)) and (x in range(8)):
                        
                        if next_field == " ":
                            has_jump.append([2,new_y,new_x])
                                                        
                            #Remove jumped piece from the board
                            board[field.y][field.x] = " "
                            set_board(board)

                            temp_piece = Piece(new_x, new_y, piece.is_white)
                            temp = check_jump(temp_piece, move_direction)
                            if len(temp)>0:
                                return temp

    return has_jump


def piece_move(piece_move_object):

    y = piece_move_object[0][1]
    x = piece_move_object[0][2]
    piece = piece_move_object[1]

    # Put piece at the new position
    board[y][x] = piece
    
    # Remove piece from old position
    piece_previous_x, piece_previous_y = piece.get_xy()
    board[piece_previous_y][piece_previous_x] = " "
    
    # Set new x and y for piece
    piece.set_yx(y,x)

    if piece.y == 7 and piece.is_white == True:
        piece.set_king()
    if piece.y == 0 and piece.is_white == False:
        piece.set_king()


# Prints board on the screen
def print_board():

    # Numerators for the board
    columns_numerators = [" 1", " 2", "3", "4 ", "5" , "6 ", "7 ", "8 "]
    print(*columns_numerators)
    i = 0

    for rows in board:
        if i==0:
            i+=1
        if 1<=i<9:
            print(i, end="")
            i+=1
        if i>9:
            pass
        print(*rows)


# Generates a board after each turn
def set_board(new_board):
    global board
    board = new_board.copy()


# Loop iterating through all pieces from most distant to the nearest row.
# if is_white = True => means its white turn
def board_loop(is_white):
        
    all_possible_moves = []

    # Sorting function
    def sort_fun(e):
        return e[0][0]

    # Checks all possible moves for piece, return list where sublist is [priority, y, x]
    # move_direction = 1 --> move down
    # move direction = -1 --> move up
    def check_move(piece, move_direction):
        y = piece.y + move_direction
        x = piece.x
        next_move = []

        # Checking is next field is available to move on
        if 0<y<8:

            # Go to next row
            row = board[y]

            # Check is next field is empty
            if (x-1>=0) and row[x-1] == " ":     # this statement should be refactored to function
                next_move.append([1, y, x-1])

            # Check is next field is empty
            if (x+1<8) and row[x+1] == " ":     # this statement should be refactored to function
                next_move.append([1, y, x+1])


            # If piece has to jump opportunity --> need testing
            if y+1<8:
                next_row = board[y+1]


        # Returns possible moves list
        return next_move

    
    # Takes list of all piece possible moves and return list where record is [move, piece]
    def make_move_object(piece, moves):

        # If piece has move
        if len(moves)>0:
            # Add move to global moves list
            for move in moves:
                new_move_object = [move, piece]
                all_possible_moves.append(new_move_object)


    # Function is iterating piece by piece checking field is piece or not. Performs moves check for each piece and make move proposition
    def fields_loop():
        for field in rows:

                # Check if field has piece on it
                if type(field)!= str:

                    # Instructions for white pieces
                    piece = field

                    if piece.is_white:

                        # Check all possible moves
                        moves = check_move(piece, 1)
                        
                        # Checks possible jumps
                        jumps = check_jump(piece, 1)

                        # Check possible jumps
                        if len(jumps)>0:
                            make_move_object(piece, jumps)

                        # Add move object [possible_move, piece_reference] to the global list of the all possible moves
                        elif len(moves)>0:
                            make_move_object(piece, moves)


                    # Instructions for black pieces
                    else:

                        # ckeck all possible moves
                        moves = check_move(piece, -1)

                        # Checks possible jumps
                        jumps = check_jump(piece, -1)

                        # Check possible jumps
                        if len(jumps)>0:
                            make_move_object(piece, jumps)

                        # Add move object [possible_move, piece_reference] to the global list of the all possible moves
                        elif len(moves)>0:
                            make_move_object(piece, moves)

                # Instructions for empty field (without piece on it)
                elif field == " ":
                    pass

    # Loop for white pieces
    if is_white != True:
        # Iterate for each row from down to up
        for rows in reversed(board):
            # Iterate for each field in a row
            fields_loop()
    
        # Sort list by move priority
        all_possible_moves.sort(reverse=True, key=sort_fun)
        
        # Pick the highest priority move
        next_move = all_possible_moves[0]

        # Move piece on the board
        piece_move(next_move)

        # Clear moves list
        all_possible_moves.clear()

    # Loop for black pieces
    elif is_white:
        for rows in board:
            fields_loop()
        
        # Sort list by move priority
        all_possible_moves.sort(reverse=True, key=sort_fun)
        
        # Pick the highest priority move
        next_move = all_possible_moves[randrange(len(all_possible_moves))]

        # Move piece on the board
        piece_move(next_move)

        # Clear moves list
        all_possible_moves.clear()