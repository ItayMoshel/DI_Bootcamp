#
# def my_abs(num):
#     storage = abs(num)
#     print(storage)
#
# def my_int(num):
#     storage = int(num)
#     print(storage)
#
# def my_input(str):
#     storage = input(str)
#     print(storage)
#
# my_abs(-11)
# my_int("11")
# my_input(11)
#


class Currency:
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount

    def __str__(self):
        storage = str(self.amount)
        storage1 = str(self.type)
        print(storage, storage1)
        return ""

    def __int__(self):
        print(self.amount)
        return 0

    def __repr__(self):
        print(f"{self.amount} {self.type}")
        return ""

    def __add__(self, other):
        print(self.amount + other)

    def __call__(self, *args, **kwargs):
        print(f"{self.amount} {self.type}")





c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

str(c1)
int(c1)
repr(c1)
c1 + 5
c1()
c1 += 5

