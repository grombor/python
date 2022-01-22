from dataclasses import field
from lib.board import make_jump, print_board, check_jump, check_move, get_board, make_move_object, piece_move
from lib.piece import Piece
from loguru import logger as log

# Get y and y coord from player
def get_coords():
    y = int(input("\nTo find field on the board: enter y-coord: "))-1
    x = int(input("To find field on the board: enter x-coord: "))-1
    return (y,x)

# Find piece on the board
def get_piece(board):
    try:
        # TODO: Check if piece is white here, validation id piece == Piece
        y, x = get_coords()
        piece = board[y][x]
        if type(piece) == Piece:
            return piece
    except IndexError:
        print(f"\nThere is no field with such coords.\n")


def fields_loop():

    n_board = get_board()
    for rows in reversed(n_board):

        for field in rows:

            # Check if field has piece on it
            if type(field)!= str:

                # Instructions for white pieces
                piece = field

                if piece.is_white:

                    # Check all possible moves
                    # moves = check_move(piece, 1)
                    
                    # Checks possible jumps
                    jumps = check_jump(piece, 1)

                    # Check possible jumps
                    if len(jumps)>0:
                        # make_move_object(piece, jumps)
                        return True

def manual_turn():
    board = get_board()
    all_possible_moves = []
    print("\nWhite pieces turn now. It is your turn.\n")
    while True:
        try:

            #field loop for players pieces
            if fields_loop():
                while True:
                    log.info("There is an obligatory jump!")

                    # Get piece
                    piece = get_piece(board)
                                    
                    # Checks possible jumps
                    jumps = check_jump(piece, 1)
                    log.debug(f"jumps: {jumps}")

                    # Get move coords
                    print("\n Where to move?\n")
                    y, x = get_coords()
                    move = [2, y, x]

                    #Check is move coords are in jump coords
                    if move in jumps:
                        log.info(f"make jump")
                        make_jump(piece, 1)
                        print_board()
                        if not fields_loop():
                            jumps = check_jump(piece, 1)
                            if len(jumps) == 0:
                                return False





            piece = get_piece(board)

            if type(piece)== Piece and piece.is_white == True:
                #NEW CODE for jumps
                
                # Check all possible moves
                moves = check_move(piece, 1)
                
                # Checks possible jumps
                # jumps = check_jump(piece, 1)

                log.debug(f"moves: {moves}")
                        

                # Check possible jumps
                # if len(jumps)>0:
                #     log.info(f"masz obowiazkowe bicie")
                #     make_jump(piece, -1)
                #     break

                # NEW CODE for standard moving

                log.debug(f"check_move(piece, 1): {moves}")

                print("\n Where to move?\n")
                y, x = get_coords()
                move = [1, y, x]
                field = board[y][x]
                if field == " " and move in moves:
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
                    break

            else: print(f"There is no piece with such coords.\n")

        except IndexError:
            print(f"There is no piece with typed coords.\n")