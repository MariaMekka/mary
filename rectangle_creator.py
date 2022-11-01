import random
from rectangle import Rectangle

class RectangleCreator:

    FIRST_SIDE_RENGE = 10
    SECOND_SIDE_RENGE = 20


    def get_rectangles(size):
        rectangles = []

        for _ in range(size):
            rect = Rectangle()
            rect.a = random.randint(1, FIRST_SIDE_RENGE)
            rect.b = random.randint(1, SECOND_SIDE_RENGE)
            rectangles.append(rect)

        return rectangles
