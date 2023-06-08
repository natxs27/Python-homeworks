import math
import pytest

class Wektor:
    def __init__(self, x, y, z):
        self.data = [x, y, z]

    def __eq__(self, other):
        return (self - other).is_zero()

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def length(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def cross(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

class TestWektor():

    def setUp(self):
        self.v = Vector(10, 5, -20)
        self.w = Vector(2, -15, 10)

    def test_vector(self):
        self.assertNotEqual(self.v, self.w)
        self.assertEqual(self.v + self.w, Vector(12, -10, -10))
        self.assertEqual(self.v - self.w, Vector(8, 20, -30))
        self.assertEqual(self.v * self.w, -255)
        self.assertEqual(self.v.cross(self.w), Vector(250, -140, -160))

if __name__ == "__main__":
    pytest.main()
