from lib.piece import Piece

p1 = Piece(1,1)

# print(p1.__str__())

# p1.move(1,2)
# p1.draw()

# print("\u250c\u2500\u2500\u2500\u2500\u2510",
#     f"\n\u2502{p1.draw()} \u2b1c\u2502",
#     "\n\u2514\u2500\u2500\u2500\u2500\u2518")

# Create a list of pieces

white_pieces_list = []
black_pieces_list = []

# The idea is:
# board = [white_pieces_list, puste_rzedy, black_pieces_list]

board = []

def generate_pieces():
    
    # Temporary list of 4 pieces and 4 white fields
    temp = []

    # Generate 1st line of white
    for field in range(1,9,2):
        new_piece = Piece(field,1,True)
        temp.append(new_piece)
        temp.append("\u2b1c")

    board.append(temp)
    temp = []

    # Generate 2nd line of white
    for field in range(2,9,2):
        new_piece = Piece(field,2,True)
        temp.append("\u2b1c")
        temp.append(new_piece)

    board.append(temp)
    temp = []

    # Generate 3nd line of white
    for field in range(1,9,2):
        new_piece = Piece(field,3,True)
        temp.append(new_piece)
        temp.append("\u2b1c")

    board.append(temp)
    temp = []

    # Generate 1st line of empty middle rows
    for field in range(2,9,2):
        temp.append("\u2b1c")
        temp.append(" ")

    board.append(temp)
    temp = []

    # Generate 2nd line of empty middle rows
    for field in range(1,9,2):
        temp.append(" ")
        temp.append("\u2b1c")

    board.append(temp)
    temp = []

    # Generate 1st line of black
    for field in range(2,9,2):
        new_piece = Piece(field,6,False)
        temp.append("\u2b1c")
        temp.append(new_piece)

    board.append(temp)
    temp = []       

    # Generate 2nd line of black
    for field in range(1,9,2):
        new_piece = Piece(field,7,False)
        temp.append(new_piece)
        temp.append("\u2b1c")

    board.append(temp)
    temp = []       

    # Generate 3nd line of black
    for field in range(2,9,2):
        new_piece = Piece(field,8,False)
        temp.append("\u2b1c")
        temp.append(new_piece)

    board.append(temp)
    temp = []       

                

generate_pieces()

for rows in board:
    print(*rows)