class Polygon:
    def __init__(self, sides_count: int):
        self.sides_count = sides_count


class Rectangle(Polygon):
    def __init__(self, width: float, height: float):
        super().__init__(4)
        self.width = width
        self.height = height

    def square(self) -> float:
        return self.width * self.height
