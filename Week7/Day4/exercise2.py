import random


def rolling_dice():
    return random.randint(1, 6)

def throw_until_double():
    flag = True
    counter = 0
    while flag:
        counter += 1
        rolling1 = rolling_dice()
        rolling2 = rolling_dice()
        # print(rolling1, rolling2)
        if rolling1 == rolling2:
            # print(f"You got doubles! {rolling1} {rolling2}")
            # print(counter)
            flag = False
    return counter

def main():
    doubles = 0
    for i in range(1, 101):
        doubles += throw_until_double()
    sum = doubles / 100
    sum_rounded = round(sum, 2)
    print(f"The average of throws made to get a double is {sum_rounded}")

main()
