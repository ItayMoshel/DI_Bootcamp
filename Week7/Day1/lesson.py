def calculation(num1, num2,):
    print(f"The numbers are: {num1}, {num2}. left is addition, right is subtraction.")
    return num1 + num2, num1 - num2

sums = calculation(100, 302)

print(sums)


def greetusers(users):
    for user in users:
        print(f"Hello {user}!")


users = ["yossi", "noam", "chen", "itay"]

greetusers(users)

def fun1():
    print("H")
def fun2():
    print("e")
def fun3():
    print("l")
def fun5():
    print("l")
def fun4():
    print("o")
lst_of_fun = [fun1, fun2, fun3, fun5, fun4]

for function in lst_of_fun:
    print(function())

things_to_do1 = ["buy glasses", "eat lunch", "drive home"]
completed_tasks = []

while len(things_to_do1) != 0:
    things_doing = things_to_do1.pop()
    print(f"Currently doing... {things_doing}")
    completed_tasks.append(things_doing)

print("\n\nThe following tasks has been done.\n")

for task_completed in completed_tasks:
    print(task_completed)

def things_to_do(notdone, dones):
    while notdone:
        taskdone = notdone.pop()
        print("Doing this..." + taskdone)
        dones.append(taskdone)

def show_done(done):
    print("\nThis is what is done: ")
    for done in dones:
        print(done)
notdone = ["a", "b", "c"]
dones = []

things_to_do(notdone, dones)
show_done(dones)
