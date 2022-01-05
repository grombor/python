from lib.board import board_loop, piece_move, generate_pieces, print_board, set_board, board

if __name__ == "__main__":

    # Variables

    # True for white pieces turn, False for black pieces turn
    white = True

    # Create board with pieces
    generate_pieces()

    # Show board on the screen
    # print_board()

    # Define moves for white pieces; is_white => True
    # Define moves for black pieces; is_white => False

    # board_loop(False)

    # print("################# 1 turn #################")

    # print_board()
    # board_loop(False)


    # print("################# 2 turn #################")

    # print_board()
    # board_loop(False)

    # print("################# 3 turn #################")
    
    # print_board()

    for i in range(10):
        print(f"\n################# {i+1}. turn #################\n")
        print_board()
        board_loop(white)
        white = not white



   
