def fib(number):
    a = 0
    b = 1
    for i in range(number + 1):
        yield a
        temp = a
        a = b
        b = temp + a


for x in fib(20):
    print(x)
