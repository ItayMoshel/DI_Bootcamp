from anagram_checker import AnagramChecker

anagram = AnagramChecker()
flag = True
while flag:
    print("Welcome to the Anagram program.")
    print("This program takes a word as an input and checks if it has an anagram.")
    user_input = input("Please input a word of your choice. else, input exit to end program.\n")
    user_input = user_input.strip()
    if user_input == "exit":
        print("Thank you and goodbye.")
        flag = False
    elif len(user_input.split()) > 1:
        print("Only one word is valid.")
        continue
    elif not user_input.isalpha():
        print("Only alphabet letters are valid.")
        continue
    else:
        if anagram.is_valid_word(user_input) == "Valid":
            print(f'Your word: "{user_input}" \nAnagram of your word: {", ".join(anagram.get_anagrams(user_input))}\n')
        else:
            print(anagram.is_valid_word(user_input))
