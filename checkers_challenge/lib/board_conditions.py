from lib.board import get_board
from lib.piece import Piece


def count_pieces(board, is_white):
    pieces = 0
    for rows in board:
        for field in rows: 
            if type(field) == Piece and field.is_white and is_white:
                pieces += 1
            if type(field) == Piece and field.is_white!=True and not is_white:
                pieces += 1

    return pieces


def check_kings(board):
    for rows in board:
        for piece in rows:
            if type(piece) == Piece:
                # Check king conditions
                if piece.y == 7 and piece.is_white == True:
                    piece.set_king()
                if piece.y == 0 and piece.is_white == False:
                    piece.set_king()


def check_pieces_on_board():

    # Variables
    board = get_board()
    white_pieces = 0
    black_pieces = 0

    #Count white pieces
    white_pieces = count_pieces(board, True)
    if white_pieces == 0:
        print("Player win!")
        quit()

    #Count black pieces
    black_pieces = count_pieces(board, False)
    if black_pieces == 0:
        print("Computer win!")
        quit()

    #Check for kings
    check_kings(board)

