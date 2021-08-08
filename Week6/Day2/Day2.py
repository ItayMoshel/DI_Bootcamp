user_name = input("select a user name.\n")
password = input("select a password\n")
password_length = len(password)

print(f"{user_name}, you'r password " + password_length * '*' + f" is {password_length} letters long.")


# selution:
    # add hidden_password = password_length * '*'.