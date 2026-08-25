import unittest
from triangle import Triangle, TriangleType

class TestTriangle(unittest.TestCase):

    def setUp(self):
        """Setup dataset fixtures for testing."""
        # Valid Triangles: (a, b, c, expected_type, expected_area)
        self.valid_triangles = [
            (5, 5, 5, TriangleType.EQUILATERAL, 10.8253),
            (5, 5, 3, TriangleType.ISOSCELES, 7.1545),
            (3, 4, 5, TriangleType.SCALENE, 6.0)
        ]

        # Invalid Triangle Inequalities (a + b <= c)
        self.invalid_inequalities = [
            (1, 2, 3),  # Degenerate triangle (1+2 = 3)
            (1, 1, 3),  # Unreachable sides (1+1 < 3)
            (10, 2, 3)
        ]

        # Zero or Negative Side Lengths
        self.invalid_lengths = [
            (0, 4, 5),
            (-1, 4, 5),
            (3, -4, 5)
        ]

        # Invalid Data Types
        self.invalid_types = [
            ("3", 4, 5),
            (None, 4, 5),
            ([3], 4, 5),
            (True, 4, 5)
        ]

    def test_valid_triangles(self):
        """Test classification and area calculation for valid triangles."""
        for a, b, c, expected_type, expected_area in self.valid_triangles:
            t = Triangle(a, b, c)
            self.assertTrue(t.is_valid(), msg=f"Triangle ({a}, {b}, {c}) should be valid.")
            self.assertEqual(t.get_type(), expected_type, msg=f"Triangle ({a}, {b}, {c}) type mismatch.")
            self.assertAlmostEqual(t.get_area(), expected_area, places=4, msg=f"Triangle ({a}, {b}, {c}) area mismatch.")

    def test_invalid_triangle_inequalities_return_false(self):
        """Test sides failing triangle inequality theorem return False."""
        for a, b, c in self.invalid_inequalities:
            t = Triangle(a, b, c)
            self.assertFalse(t.is_valid(), msg=f"Triangle ({a}, {b}, {c}) should be invalid.")
            self.assertIsNone(t.get_type())
            self.assertIsNone(t.get_area())

    def test_zero_or_negative_sides_return_false(self):
        """Test zero or negative sides return False."""
        for a, b, c in self.invalid_lengths:
            t = Triangle(a, b, c)
            self.assertFalse(t.is_valid(), msg=f"Triangle ({a}, {b}, {c}) should be invalid.")

    def test_invalid_types_return_false(self):
        """Test non-numeric input types return False."""
        for a, b, c in self.invalid_types:
            t = Triangle(a, b, c)
            self.assertFalse(t.is_valid(), msg=f"Input ({a}, {b}, {c}) contains invalid type and should return False.")


if __name__ == '__main__':
    unittest.main()