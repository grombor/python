from .piece import Piece
from random import randrange


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
all_possible_moves = []
has_jumped = False

def get_board():
    return board

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
    """
        Function takes piece instance nad move direction (+1 for white pieces going down on the board; -1 for black pieces going up on the board). Checks is any possibility of jumps.

    """


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
                if new_y in range(8) and new_x in range(8):

                    # Get the next row diagonal left field
                    next_field = board[new_y][new_x]

                    if next_field == " ":
                        next_move = [2, new_y, new_x]
                        has_jump.append(next_move)


        if right in range(8):

            # Go check next row, check field on the diagonal left
            field = board[y+move_direction][x+1]

            # Check is there a piece and
            # Check is the different color than current piece
            if type(field) == Piece and field.is_white != piece.is_white:

                # Go to next row next field on the right
                new_y = y+2*move_direction
                new_x = right+1
                if new_y in range(8) and new_x in range(8):
                    next_field = board[new_y][new_x]

                    if next_field == " ":
                        next_move = [2, new_y, new_x]
                        has_jump.append(next_move)

    return has_jump


def make_jump(piece, move_direction):
    next_moves = check_jump(piece, move_direction)
    n_board = get_board()
    if len(next_moves)>0:
        # Choose move
        move = randrange(0,len(next_moves))

        y = int(piece.y)+int(move_direction)
        x = int((int(next_moves[move][2])+int(piece.x))/2)

        n_board[y][x] = " "

        n_board[piece.y][piece.x] = " "


        y = next_moves[move][1]
        x = next_moves[move][2]
        piece.set_yx(y, x)
        n_board[y][x] = piece
        set_board(n_board)


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


# Prints board on the screen
def print_board():

    # Numerators for the board
    print("\n")

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
# value "True" means its white turn
def board_loop(is_white):
        
    def pick_move(all_possible_moves):
        return randrange(len(all_possible_moves))


    # Function is iterating piece by piece checking field is piece or not. Performs moves check for each piece and make move 
    def fields_loop():
        global has_jumped

        
        for field in rows:

            if (type(field) == Piece) and (not field.is_white):

                
                # ckeck all possible moves
                moves = check_move(field, -1)

                # Checks possible jumps
                jumps = check_jump(field, -1)
                        
                # Make jump if possible
                if len(jumps)>0:
                    make_jump(field, -1)
                    moves.clear()
                    has_jumped = True
                    return False


                make_move_object(field, moves)


    # Loop for white pieces
    if is_white != True:
        global has_jumped
        has_jumped = False

        # Iterate for each row from down to up
        for rows in reversed(board):
            # Iterate for each field in a row
            fields_loop()

        if len(all_possible_moves) == 0:
            return False
        
        pmove = pick_move(all_possible_moves)

        # Pick the highest priority move
        next_move = all_possible_moves[pmove]


        # Move piece on the board
        if not has_jumped:
            piece_move(next_move)

        # Clear moves list
        all_possible_moves.clear()



