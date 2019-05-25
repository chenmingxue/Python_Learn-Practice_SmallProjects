#single inheritance 1
class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def circumstance(self):
        return (self.length + self.width)*2

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
    def isSquare(self):
        return self.length == self.width

class Cube(Square):
    def surfaceArea(self):
        self.face_area = super(Cube, self).area() #super(thisClass,self) = super()
        return self.face_area * 6

    def volume(self):
        return self.length * self.face_area
length = int(input("Please key in the length: "))
square = Square(length)
print(square.area())
print(square.circumstance())
print(square.isSquare())
cube = Cube(length)
print(cube.surfaceArea())
print(cube.volume())
print(Cube.__mro__) #this is to check method resolution order
