import datetime


def current_date():
    print(datetime.datetime.now())


current_date()


def time_till_jan1():
    print(datetime.datetime(2022, 1, 1) - datetime.datetime.now())


time_till_jan1()


def min_alive(date):
    birthday_list = date.split("/")
    birthday_year = int(birthday_list[0])
    birthday_month = int(birthday_list[1])
    birthday_day = int(birthday_list[2])
    birth_day = datetime.date(birthday_year, birthday_month, birthday_day)
    time_alive = datetime.date.today() - birth_day
    time_alive_str = str(time_alive)
    container = time_alive_str.split(" ")
    time_alive_int = int(container[0])
    minutes_alive = time_alive_int * 24 * 60
    print(f"Minutes alive: {minutes_alive}")


min_alive("1990/07/28")
