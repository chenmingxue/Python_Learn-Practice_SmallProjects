#Write a Python class named Rectangle constructed by a length and width and a method which will compute
#the area of a rectangle. - Go to the editor
class RectangleArea:
    def __init__(self):
        self.length = 0
        self.width = 0

    def set_parameters(self, input_length, input_width):
        self.length = float(input_length)
        self.width = float(input_width)

    def get_area(self):
        return self.length*self.width


if __name__ == "__main__":
    input_length = input("Please key in the length: ")
    input_width = input("Please key in the width: ")
    rectangle = RectangleArea()
    rectangle.set_parameters(input_length, input_width)
    print (rectangle.get_area())
