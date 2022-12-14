class Rectangle:

    def __init__(self, a=1, b=1):
         self.a = a
         self.b = b

    def calculate_square(self):
        return self.a * self.b

    def calculator_perimeter(self):
        return (self + self.b) * 2

    def get_info(self):
        return f"Rectangle : a = {self.a}, b = {self.b}"

    def __del__(self):
         pass

rect1 = Rectangle(10, 15)
rect2 = Rectangle(54, 504)
rect3 = Rectangle(87, 96)
rect4 = Rectangle()

print(rect1.get_info())
print(rect2.get_info())
print(rect3.get_info())
print(rect4.get_info())

