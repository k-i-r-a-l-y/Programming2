import math

class HalmazHatarertekek:

    def __init__(self,list):
        self.s = set(list)

    def keres(self):
        self.minimum = math.inf
        self.maximum = - math.inf

        for item in self.s:
            if item > self.maximum:
                self.maximum = item
            if item < self.minimum:
                self.minimum = item
        return self.minimum, self.maximum

class Piramis:

    def __init__(self, num):
        self.n = num

    def epit(self):
        for i in range(1, self.n + 1):
            if i <=self.n // 2:
                print(i * '*')
            else:
                print((self.n + 1 - i) * '*')

import numpy as np
class Matrix:

    def __init__(self,sor, oszlop):
        self.n = sor
        self.m = oszlop
        self.mtx = np.zeros((self.n,self.m))

    def feltolt(self):
        for i in range(self.n):
            for j in range(self.m):
                self.mtx[i,j] = i * j
        print(self.mtx)

m1 = Matrix(3,4)
m2 = Matrix(2,5)
m3 = Matrix(12,10)

m3.feltolt()

# p1 = Piramis(5)
#
# p2 = Piramis(15)
# p1.epit()
# print('\n')
# p2.epit()
#
# halmaz_1 = HalmazHatarertekek([2,2,4,8,-3])
# halmaz_2 = HalmazHatarertekek([2,4,8,-3])
# halmaz_3 = HalmazHatarertekek([2,21,4,888,-3])
#
# print(halmaz_3.keres())