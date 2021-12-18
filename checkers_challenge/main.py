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
# pieces_list = [white_pieces_list, black_pieces_list]

def generate_pieces(color):
    if color == "white":
        for i in range(1,9,2):
            p0 = piece.Piece(1, i, True)
            white_pieces_list.append(p0)
        for i in range(2,9,2):
            p0 = piece.Piece(2, i, True)
            white_pieces_list.append(p0)
        for i in range(1,9,2):
            p0 = piece.Piece(3, i, True)
            white_pieces_list.append(p0)
    if color != "white":
        for i in range(2,9,2):
            p0 = piece.Piece(6, i, False)
            black_pieces_list.append(p0)
        for i in range(1,9,2):
            p0 = piece.Piece(7, i, False)
            black_pieces_list.append(p0)
        for i in range(2,9,2):
            p0 = piece.Piece(8, i, False)
            black_pieces_list.append(p0)

generate_pieces("white")
generate_pieces("bla")

print (f"############ WHITE ##############")
for l in white_pieces_list:
    print(l)

print (f"############ BLACK ##############")

for b in black_pieces_list:
    print(b)
