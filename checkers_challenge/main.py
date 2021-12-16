from lib import piece

p1 = piece.Piece(1,1)

print(p1.__str__())

p1.move(1,2)
print(p1.draw())

print("\u250c\u2500\u2500\u2500\u2500\u2510",
    f"\n\u2502{p1.draw()} \u2b1c\u2502",
    "\n\u2514\u2500\u2500\u2500\u2500\u2518")