class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):    # return string "Vector(x, y, z)"
        return 'Vector ({}, {}, {})'.format(self.x, self.y, self.z)

    def find_axis(self, w):
        if self.x == w.x and self.y == w.y and self.z == w.z: 
            raise ValueError("The vector is parallel and not perpendicular")
        elif self.x == 0 and self.y == 0 and self.z == 0:
            raise ValueError("The vector is parallel and not perpendicular")
        elif w.x == 0 and w.y == 0 and w.z == 0:
            raise ValueError("The vector is parallel and not perpendicular")
        else:
            return Vector(self.y * w.z - self.z * w.y,
                          self.z * w.x - self.x * w.z,
                          self.x * w.y - self.y * w.x)
v = Vector(1, 2, 3)
#v = Vector(0, 0, 0)
w = Vector(2, -3, 2)
#w = Vector(0, 0, 0)
#w = Vector(1, 2 ,3)
        
print(v.find_axis(w))
