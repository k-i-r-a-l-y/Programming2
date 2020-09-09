import math

#1. feladat

maximum = -math.inf
minimum = math.inf

s = {21,4,-3,5,9,88,3,-21,2}

for item in s:
    if item > maximum:
        maximum = item
    if item < minimum:
        minimum = item

print(minimum, maximum)

#2. feladat

n = int(input("Kerek egy szamot:"))

for i in range(1, n+1):
    if i <= n//2:
        print(i * '*')
    else:
        print((n + 1 - i) * '*')

#3. feladat

import numpy as np

sor = int(input("Kerem a sorok szamat:"))
oszlop = int(input("Kerem az oszlopok szamat:"))

mtx = np.zeros((sor, oszlop))

for i in range(sor):
    for j in range(oszlop):
        mtx[i,j] = i * j

print(mtx)