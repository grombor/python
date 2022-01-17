from lib.board import board_loop, manual_turn, piece_move, generate_pieces, print_board, set_board, board

if __name__ == "__main__":

    # Create board with pieces
    generate_pieces()

    # white = True

    # for i in range(20):
    #     print(f"\n################# {i+1}. turn #################\n")
    #     print_board()
    #     board_loop(white)
    #     white = not white

    turn_counter = 0

    while True:
        turn_counter += 1
        print(f"\n################# {turn_counter}. turn #################\n")
        manual_turn()
        print("Computer turn:")
        board_loop(False)
        print_board()
        break



   
