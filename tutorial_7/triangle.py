# triangle.py
import math
from enum import Enum

class TriangleType(Enum):
    EQUILATERAL = "Equilateral"
    ISOSCELES = "Isosceles"
    SCALENE = "Scalene"

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self) -> bool:
        """
        Validates if the three sides can form a valid triangle.
        - Inputs must be integers or floats.
        - Sides must be greater than 0.
        - Triangle inequality theorem: sum of any two sides > third side.
        """
        # Type Check
        if not (isinstance(self.a, (int, float)) and 
                isinstance(self.b, (int, float)) and 
                isinstance(self.c, (int, float))) or \
           isinstance(self.a, bool) or isinstance(self.b, bool) or isinstance(self.c, bool):
            print("Side lengths must be numbers.")
            return False

        # Positive Length Check
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            print("Side lengths must be greater than zero.")
            return False

        # Triangle Inequality Theorem Check
        if (self.a + self.b <= self.c) or (self.a + self.c <= self.b) or (self.b + self.c <= self.a):
            print("The sum of any two sides must be strictly greater than the third side.")
            return False

        return True

    def get_type(self):
        """Classifies the triangle type."""
        if not self.is_valid():
            return None

        if self.a == self.b == self.c:
            return TriangleType.EQUILATERAL
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return TriangleType.ISOSCELES
        else:
            return TriangleType.SCALENE

    def get_area(self):
        """Calculates area using Heron's Formula."""
        if not self.is_valid():
            return None

        s = (self.a + self.b + self.c) / 2.0
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return round(area, 4)


if __name__ == '__main__':
    try:
        a = float(input("Enter side A: "))
        b = float(input("Enter side B: "))
        c = float(input("Enter side C: "))
        
        t = Triangle(a, b, c)
        if t.is_valid():
            print(f"Triangle Type: {t.get_type().value}")
            print(f"Triangle Area: {t.get_area()}")
        else:
            print("Invalid triangle parameters.")
    except ValueError:
        print("Invalid input! Please enter numeric values.")