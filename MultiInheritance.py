class Rectangle():
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)

    def area(self):
        return self.length * self.width

    def circumstance(self):
        return (self.length + self.width) * 2

class Square(Rectangle):
    def __init__(self, length, **kwargs):
        super().__init__(length=length, width=length, **kwargs)

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

cube = Cube(3)
print(cube.circumstance())
print(cube.volume())
print('*' * 20)

class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)

    def tri_area(self):
        return 0.5 * self.base * self.height


class Pyramid(Square, Triangle): #multiple super class, here **kwargs is used 
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs["height"] = slant_height
        kwargs["length"] = base
        super().__init__(base=base, **kwargs)

    def pyr_area1(self):
        base_area = super().area()
        perimeter = super().circumstance()
        return 0.5 * perimeter * self.slant_height + base_area

    def pyr_area2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area

pyramid = Pyramid(3, 2)
print(pyramid.pyr_area1())
print(pyramid.pyr_area2())

