from lib.board import board_loop, piece_move, generate_pieces, print_board, set_board, board

if __name__ == "__main__":

    generate_pieces()
    print_board()

    # pionek
    # zmienna popnka z 2,0
    piece = board[2][0]
    # print(piece)
    print(piece.y, piece.x, piece.is_white)
    # end pionke

    print("\n####### tura 1 #############\n")
    piece_move(piece, 3, 1)
    print_board()
    print(piece.y, piece.x, piece.is_white)
    


    print("\n####### tura 2 #############\n")
    piece_move(piece, 4, 0)
    print_board()
    print(piece.y, piece.x, piece.is_white)
    
   
