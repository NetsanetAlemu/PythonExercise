class Rectangle:

    def __init__(self, length, witdth):
        self.length = length
        self.width = witdth

    def rectangle_perimeter(self):
        return 2 * (self.length + self.width)
    def rectangle_area(self):
        return self.length * self.width
   
 
