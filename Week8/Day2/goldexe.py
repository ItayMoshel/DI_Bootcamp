class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        perimeter = self.radius * 2 * 3.14
        print(perimeter)

    def area(self):
        area = self.radius ** 2 * 3.14
        print(area)


circle1 = Circle()

circle1.perimeter()
circle1.area()


class Mylist:
    def __init__(self, my_list):
        self.my_list = list(my_list)

    def rev_list(self):
        self.my_list.reverse()
        return self.my_list

    def sort_list(self):
        self.my_list.sort()
        return self.my_list


aaa = Mylist([3, 8, 1, 2])
print(aaa.rev_list())
print(aaa.sort_list())
