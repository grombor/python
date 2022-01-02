from lib.board import board_loop, piece_move, generate_pieces, print_board, set_board, board

if __name__ == "__main__":

    # Create board with  pieces
    generate_pieces()

    # Show board on the screen
    print_board()

    # Define moves for white pieces; Black pieces still TODO
    # is_white => True
    board_loop(True)

    print("################# 1 turn #################")

    print_board()
    board_loop(True)


    print("################# 2 turn #################")

    print_board()
    board_loop(True)

    print("################# 3 turn #################")
    
    print_board()

   
