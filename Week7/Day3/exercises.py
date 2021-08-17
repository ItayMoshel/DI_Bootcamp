my_list = [2, 3, 1, 2, "four", 42, 1, 5, 3, "imanumber"]

def list_iterator():
    sum = 0
    for item in my_list:
        try:
            sum += item
        except:
            continue
    return sum

print(list_iterator())