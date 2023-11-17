class Square:
    def __init__(self, length):
        self.length = length
    def square_perimeter(self):
        return 4 * self.length
    def square_area(self):
        return self.length * self.length