from volume import Volume

class Rectangular_prism(Volume):

    def __init__(self, height, length, width):
        self.height = height
        self.length = length
        self.width = width
    
    def area(self):
        return self.width * self.length 

    