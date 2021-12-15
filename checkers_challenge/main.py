from lib import piece

p1 = piece.Piece(1,1)

print(p1.__str__())

p1.move(1,2)
print(p1.symbol())