from volume import Volume

class Cylinder(Volume):

    def __init__(self, height, radius):
        self.height = height
        self.radius = radius
    
    def area(self):
        return self.radius * self.radius * 3.14

    