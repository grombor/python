from lib import piece

p1 = piece.Piece(1,1)

# print(p1.__str__())

p1.move(1,2)
p1.draw()

# print("\u250c\u2500\u2500\u2500\u2500\u2510",
#     f"\n\u2502{p1.draw()} \u2b1c\u2502",
#     "\n\u2514\u2500\u2500\u2500\u2500\u2518")

# Create a list of pieces

white_pieces_list = []
black_pieces_list = []

# The idea is:
# board = [white_pieces_list, puste_rzedy, black_pieces_list]

row1, row2, row3, row4, row5, row6, row7, row8 = [],[],[],[],[],[],[],[]
board = [
    row1, 
    row2,
    row3,
    row4,
    row5,
    row6,
    row7,
    row8
    ]

def generate_pieces(is_white):
    for row in board:
        for i in range(0,8):
            # p0 = piece.Piece(is_white)
            # row.append(p0)
            row.append("\u2b1c")
            row.append("\u2b1b")
                

generate_pieces(True)

for row in board:
    for r in row:
        print(r)