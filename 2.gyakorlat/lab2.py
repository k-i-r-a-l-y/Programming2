

class Szam:

    def __init__(self,num):
        self.n = num

    def square_n(self):
        return self.n ** 2

    def pow_k(self, k):
        return self.n ** k

    def absolute_value(self):
        if self.n >= 0:
            return self.n
        else:
            return -self.n

class Circle:

    def __init__(self, radius):
        self.r = radius

    def get_perimeter(self):
        import math
        return 2 * self.r * math.pi

    def get_area(self):
        import math
        return self.r ** 2 * math.pi

    def __str__(self):
        return "Radius: {}\nKerulet: {}\nTerulet: {}".format(self.r,self.get_perimeter(),self.get_area())

class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_perimeter(self):
        return 2 * (self.a + self.b)

    def get_area(self):
        return self.a * self.b

    def __str__(self):
        return f"A oldal: {self.a}\nB oldal: {self.b}\nKerulet: {self.get_perimeter()}\nTerulet: {self.get_area()}"

class Szoveg:

    str = "Ez az alapertelmezett string"
    def __init__(self):
        pass

    def set_string(self):
        self.str = input("Kerek egy uj stringet: ")

    def print_string(self):
        print(self.str.upper())

class Szamlista:

    def __init__(self,lista):
        self.lista = lista

    def sum_zero(self):
        result_list = []
        for i in range(len(self.lista)):
            for j in range(i+1,len(self.lista)):
                for k in range(j + 1, len(self.lista)):
                    if self.lista[i] + self.lista[j] + self.lista[k] == 0:
                        result_list.append([self.lista[i],self.lista[j],self.lista[k]])
        print(result_list)

#1.feladat
# szam1 = Szam(5)
# print(szam1.square_n())
# szam2 = Szam(13)
# print(szam2.pow_k(3))

#2.feladat
# c1 = Circle(3)
# print(c1.get_area())
# print(c1)

#3.feladat

# teglalap1 = Rectangle(2,3)
# print(teglalap1)

#4.feladat
# s1 = Szoveg()
# print(s1.str)
# s1.set_string()
# s1.print_string()

#5.feladat
szamok = Szamlista([-25, -10, -7, -3, 2, 4, 8, 10])
szamok.sum_zero()
