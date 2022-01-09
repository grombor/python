from lib.board import board_loop, piece_move, generate_pieces, print_board, set_board, board

if __name__ == "__main__":

    # Variables

    # True for white pieces turn, False for black pieces turn
    white = True

    # Create board with pieces
    generate_pieces()

    for i in range(20):
        print(f"\n################# {i+1}. turn #################\n")
        print_board()
        board_loop(white)
        white = not white



   
