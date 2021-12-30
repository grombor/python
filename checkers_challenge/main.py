from lib.board import board_loop, piece_move, generate_pieces, print_board, set_board, board

if __name__ == "__main__":

    # Create board with  pieces
    generate_pieces()

    # Show board on the screen
    print_board()

    # Define moves for white pieces; Black pieces still TODO
    # is_white => True
    board_loop(True)


    # pionek
    # instancja pionka z 2,0
    # piece = board[2][0]
    # print(piece)
    # print(piece.y, piece.x, piece.is_white)
    # end pionek

    # print("\n####### tura 1 #############\n")
    # piece_move(piece, 3, 1)
    # print_board()
    # print(piece.y, piece.x, piece.is_white)
    


    # print("\n####### tura 2 #############\n")
    # piece_move(piece, 4, 0)
    # print_board()
    # print(piece.y, piece.x, piece.is_white)
    
   
