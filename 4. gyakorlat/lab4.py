

class Polygon:

    side_length = []

    def __init__(self, n):
        self.sides = n

    def input_sides(self):
        for i in range(self.sides):
            side = int(input("Kerem az {}. oldal hosszat:".format(i+1)))
            self.side_length.append(side)

    def disp_sides(self):
        for i in range(self.sides):
            print("Az {}. oldal hossza: {}".format(i+1,self.side_length[i]))

class Triangle(Polygon):

    def __init__(self):
        Polygon.__init__(self, 3)

    def triangle_check(self):
        a, b, c = self.side_length[0], self.side_length[1], self.side_length[2]
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            return False
        return True

    def input_sides(self):
        while True:
            self.side_length = []
            super().input_sides()
            if self.triangle_check():
                break
            else:
                print("Hibas oldalhosszok!")

    def get_perimeter(self):
        res = 0
        for i in range(self.sides):
            res += self.side_length[i]
        return res

class BankAccount:

    def __init__(self, money):
        self.egyenleg = money

    def deposit(self, money):
        self.egyenleg += money
        print(self)

    def withdraw(self, money):
        self.egyenleg -= money
        print(self.__str__())

    def __str__(self):
        return "A jelenlegi egyenleg: {}Ft.".format(self.egyenleg)

class MinBankAccount(BankAccount):

    def __init__(self, p1, p2):
        while p2 >= p1:
            p1 = int(input("Kerek egy masik osszeget: "))
        super().__init__(p1)
        self.min_value = p2

    def withdraw(self, money):
        if self.egyenleg - money < self.min_value:
            print("Nincs eleg penz a szamlan a tranzakcio vegrehajtasahoz!")
        else:
            BankAccount.withdraw(self, money)

class MyList(list):

    def __init__(self, p1):
        super().__init__(p1)

    def print_items_with_indices(self):
        for idx, item in enumerate(self):
            print("{}.elem: {}".format(idx, item))

    def append(self, p1):
        super().append(p1 + 5)

lista1 = MyList([2,4])
lista1.print_items_with_indices()
lista1.append(5)
print(lista1)

# p1 = Polygon(5)
# p1.input_sides()
# p1.disp_sides()
#
# t1 = Triangle()
# t1.input_sides()
# t1.disp_sides()

# b1 = MinBankAccount(50,1000)
# b1.deposit(500)






