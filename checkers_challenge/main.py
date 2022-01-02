from lib.board import board_loop, piece_move, generate_pieces, print_board, set_board, board

if __name__ == "__main__":

    # Create board with  pieces
    generate_pieces()

    # Show board on the screen
    # print_board()

    # Define moves for white pieces; is_white => True
    # Define moves for black pieces; is_white => False

    board_loop(False)

    print("################# 1 turn #################")

    print_board()
    board_loop(False)


    print("################# 2 turn #################")

    print_board()
    board_loop(False)

    print("################# 3 turn #################")
    
    print_board()

   
