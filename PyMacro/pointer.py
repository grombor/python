class Pointer:
    
    def __init__(self, x, y, time) -> None:
        self.x_pos = x    
        self.y_pos = y
        self.time = time

    def __str__(self):
        return f'Point: X: {self.x_pos}, Y: {self.y_pos}, Time: {self.time}'
