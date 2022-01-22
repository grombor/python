from lib.board import board_loop, piece_move, generate_pieces, print_board, set_board, board
from lib.human import manual_turn

if __name__ == "__main__":

    # Create board with pieces
    generate_pieces()

    # white = True

    # Code for AI vs AI battle
    # for i in range(20):
    #     print(f"\n################# {i+1}. turn #################\n")
    #     print_board()
    #     board_loop(white)
    #     white = not white

    turn_counter = 0

    while True:
        turn_counter += 1

        print(f"\n################# {turn_counter}. turn #################\n")

        print("\nPlayer's turn:")

        print_board()
        manual_turn()
        print_board()

        print("\nComputers turn:")
        board_loop(False)




   
