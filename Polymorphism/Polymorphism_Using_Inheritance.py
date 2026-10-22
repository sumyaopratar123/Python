class Shape:
    def area(self):
        print("Area of shape")

class Square(Shape):
    def area(self):
        side = 5
        print("Area of Square =", side * side)

class Rectangle(Shape):
    def area(self):
        length = 4
        breadth = 6
        print("Area of Rectangle =", length * breadth)

s = Square()
r = Rectangle()

s.area()
r.area()