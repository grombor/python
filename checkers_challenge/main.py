from lib.board import board_loop, generate_pieces, print_board, set_board, board

if __name__ == "__main__":
    generate_pieces()
    # print_board()

    # Test: make a new board
    # new_board = [["\u2b50", "\u2b50"], ["\u2b50", "\u2b50"]]

    # Test: set up new board
    # set_board(new_board)

    # Test: print a new board
    # print_board()

    row = board[0]
    column = row[0]

    board_loop(True)

    column.get_moves()
