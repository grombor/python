from lib.board import print_board, check_jump, check_move, get_board, make_move_object, piece_move
from lib.piece import Piece
from loguru import logger as log

def manual_turn():
    board = get_board()
    all_possible_moves = []
    print("White pieces turn now. It is your turn.\n")
    while True:
        print_board()
        try:
            y = int(input("\nChoose piece: enter y-coord for piece: "))-1
            x = int(input("Choose piece: enter x-coord for piece: "))-1
            piece = board[y][x]

            if type(piece) == Piece and piece.is_white == True:
                jumps = check_jump(piece, 1)

                if len(jumps)>0:
                    print(f"You are obligated to jump.")
                    make_move_object(piece, jumps)

                    # Pick the highest priority move
                    next_move = all_possible_moves[0]

                    # Move piece on the board
                    piece_move(next_move)

                    # Clear moves list
                    all_possible_moves.clear()

                    print_board()
                    break

                else:
                    temp = check_move(piece, 1)
                    print(temp)
                    print("\n Where to move?")
                    y = int(input("\nChoose piece: enter y-coord: "))-1
                    x = int(input("Choose piece: enter x-coord: "))-1
                    move = board[y][x]
                    if move == " ":
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
            else: print(f"There is no piece with typed coords.\n")

        except IndexError:
            print(f"There is no piece with typed coords.\n")