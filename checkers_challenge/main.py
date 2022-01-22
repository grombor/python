from lib.board import board_loop, generate_pieces, print_board
from lib.board_conditions import check_pieces_on_board
from lib.human import manual_turn
from time import sleep

if __name__ == "__main__":

    # Create board with pieces
    generate_pieces()

    turn_counter = 0

    while True:
        turn_counter += 1

        print(f"\n################# {turn_counter}. turn #################\n")

        print("\nPlayer's turn:\n")

        print_board()
        manual_turn()
        check_pieces_on_board()

        print("\nComputers turn:\n")

        print_board()
        sleep(1.5)
        board_loop(False) # Value "False" indicates to make move as Black Pieces
        check_pieces_on_board()





   
