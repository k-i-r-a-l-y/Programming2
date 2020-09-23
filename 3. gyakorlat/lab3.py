

class Triangle:

    def __init__(self, p1, p2, p3 = 0):
        if p3 == 0:
            self.a = p1
            self.m = p2
        else:
            self.a = p1
            self.b = p2
            self.c = p3

    def perimeter(self):
        if hasattr(self, 'c'):
            return self.a + self.b + self.c
        else:
            return "A megadott parameterekkel nem szamolhato a kerulet!"

    def area(self):
        if hasattr(self, 'c'):
            s = (self.a + self.b + self.c) / 2
            return (s * (s - self.a) * (s - self.b) * (s - self.c))**0.5
        else:
            return (self.a * self.m) / 2

    def __str__(self):
        if hasattr(self, 'c'):
            return f"a: {self.a}\nb: {self.b}\nc: {self.c}\nkerulet: {self.perimeter()}\nterulet: {self.area()}"
        else:
            return f"alap: {self.a}\nmagassag: {self.m}\nTerulet: {self.area()}"

    def __add__(self, other):
        if isinstance(other, Triangle):
            return self.area() + other.area()
        elif isinstance(other, int) or isinstance(other, float):
            return self.area() + other

    def __sub__(self, other):
        if isinstance(other, Triangle):
            return self.area() - other.area()
        elif isinstance(other, int) or isinstance(other, float):
            return self.area() - other

    def __radd__(self, other):
        return self.__add__(other)

    def __eq__(self, other):
        if isinstance(other, Triangle):
            return self.perimeter() == other.perimeter()
        else:
            return "A ket objektum nem osszehasonlithato"

    def __ne__(self, other):
        if isinstance(other, Triangle):
            return self.perimeter() != other.perimeter()
        else:
            return "A ket objektum nem osszehasonlithato"

    def __gt__(self, other):
        if isinstance(other, Triangle):
            return self.perimeter() > other.perimeter()
        else:
            return "A ket objektum nem osszehasonlithato"

    def __lt__(self, other):
        if isinstance(other, Triangle):
            return self.perimeter() <= other.perimeter()
        else:
            return "A ket objektum nem osszehasonlithato"

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5

    def __str__(self):
        return "<{}, {}>".format(self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
            return self
        elif isinstance(other, int) or isinstance(other,float):
            self.x += other
            self.y += other
            return self

    def __sub__(self, other):
        if isinstance(other, Vector):
            self.x -= other.x
            self.y -= other.y
            return self
        elif isinstance(other, int) or isinstance(other,float):
            self.x -= other
            self.y -= other
            return self

    def __mul__(self, other):
        if isinstance(other, Vector):
            self.x *= other.x
            self.y *= other.y
            return self
        elif isinstance(other, int) or isinstance(other,float):
            self.x *= other
            self.y *= other
            return self

    def __eq__(self, other):
        return self.__abs__() == other.__abs__()

    def __ne__(self, other):
        return self.__abs__() != other.__abs__()

    def __gt__(self, other):
        return self.__abs__() > other.__abs__()

    def __lt__(self, other):
        return self.__abs__() < other.__abs__()

    def __iadd__(self, other):
        return self.__add__(other)


# t1 = Triangle(3,4,5)
# t2 = Triangle(4,5,3)
# print(t1)

v1 = Vector(2,3)
v2 = Vector(1,1)
print(v1 - 1)