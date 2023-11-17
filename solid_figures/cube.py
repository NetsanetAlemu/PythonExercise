from volume import Volume

class Cube(Volume):

    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length * self.length

    

