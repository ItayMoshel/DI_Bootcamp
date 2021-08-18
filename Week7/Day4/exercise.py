from datetime import datetime

def get_age(year, month, day):
    current_date = datetime.today().strftime('%Y-%m-%d')
    current_date_list = current_date.split("-")
    current_year = int(current_date_list[0])
    current_month = int(current_date_list[1])
    current_day = int(current_date_list[2])
    user_age = current_year - year -1
    if current_month > month and current_day > day:
        user_age =+ 1

    return user_age

#having truble with the day and month calculation.

def can_retire(gender, *date_of_birth):
    user_age = get_age(*date_of_birth)
    if gender == "m":
        return user_age >= 67
    elif gender == "f":
        return user_age >= 62

print(can_retire("m", 1954, 7, 28))



def summer(x):
    sum = 0
    x_as_str = str(x)
    for i in range(1, 5):
        x_num = x_as_str * i
        x_as_int = int(x_num)
        sum += x_as_int
    print(sum)

summer(3)







