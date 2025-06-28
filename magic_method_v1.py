import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector2D(x={self.x}, y={self.y})"

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y  # Dot Product

    def __len__(self):
        return int(math.sqrt(self.x ** 2 + self.y ** 2))  # Magnitude as integer

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __call__(self):
        print(f"Coordinates are: ({self.x}, {self.y})")

# -------------------
# Test it
# -------------------

v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

print(v1)                # Vector(3, 4)
print(repr(v2))           # Vector2D(x=1, y=2)
print(v1 + v2)            # Vector(4, 6)
print(v1 - v2)            # Vector(2, 2)
print(v1 * v2)            # Dot product => (3*1 + 4*2) = 11
print(len(v1))            # Magnitude => 5
print(v1 == v2)           # False
print(v1 != v2)           # True
v1()                     # Callable object
