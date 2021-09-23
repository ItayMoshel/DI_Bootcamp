# with open('lesson.2.py', 'w') as f:
#     for i in range(11):
#         f.write("# this is line: %i\n" % i)
#
# for line in open('lesson.2.py'):
#     print(line)

# with open("lesson.2.py", 'a') as f:
#     lines = ["\nhello ", "how ", "are ", "you ", "?"]
#     f.writelines(lines)

# with open('text.txt', 'r') as f:
#     print(f.read())

# with open('text.txt', 'r') as f:
#     files = f.readlines()
#     print(files[4])

# with open('text.txt', 'r') as f:
#     files = f.readlines()
#     for i in range(0, 5):
#         print(files[i])

# with open('text.txt', 'r') as f:
#     files = f.readlines()
#     for item in files:
#         print(item.split("\'"))
#     print(files)

# with open('text.txt', 'r') as f:
#     files = f.readlines()
#     Luke = 0
#     Lea = 0
#     Darth = 0
#     for line in files:
#         if line == "Luke\n":
#             Luke += 1
#     for line in files:
#         if line == "Lea\n":
#             Lea += 1
#     for line in files:
#         if line == "Darth\n" or line == "Darth":
#             Darth += 1
#
#     print(f"Luke: {Luke}, Lea: {Lea}, Darth: {Darth}")
#     print("Luke: ", files.count("Luke\n"))
#     print("Lea: ", files.count("Lea\n"))
#     print("Darth: ", files.count("Darth\n") + files.count("Darth"))

# with open("text.txt", "a+") as f:
#     f.write("\nItay moshel.")
#     file = f.read().splitlines()
#     for i in range(len(file)):
#         if file[i] == "Luke":
#             file.insert(i+1, "SkyWalker")
#


