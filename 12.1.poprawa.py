import math
import unittest

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def cross(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

class TestVector(unittest.TestCase):
    def setUp(self):
        self.v = Vector(1, 2, -2)
        self.w = Vector(2, -1, 1)

    def test_vector_equality(self):
        self.assertEqual(self.v, Vector(1, 2, -2))
        self.assertNotEqual(self.v, self.w)

    def test_vector_addition(self):
        result = self.v + self.w
        self.assertEqual(result, Vector(3, 1, -1))

    def test_vector_subtraction(self):
        result = self.v - self.w
        self.assertEqual(result, Vector(-1, 3, -3))

    def test_vector_multiplication(self):
        result = self.v * self.w
        self.assertEqual(result, -255)

    def test_vector_cross_product(self):
        result = self.v.cross(self.w)
        self.assertEqual(result, Vector(0, -5, -5))

if __name__ == "__main__":
    unittest.main()
