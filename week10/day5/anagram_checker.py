# with open("sowpods.txt", "r") as text:
#     word_to_check = input("Please input a word.")
#     word_in_text = text.read().splitlines()
#     if word_to_check in word_in_text:
#         print("Hey")
#     input_list = list(word_to_check)
#     input_list.sort()
#     anagram_list = []
#     for item in word_in_text:
#         item_list = list(item)
#         item_list.sort()
#         if item_list == input_list:
#             anagram_list.append(item)
#     print(anagram_list)

class AnagramChecker:
    def __init__(self):
        with open("sowpods.txt", "r+") as file_obj:
            self.file = file_obj.read().splitlines()

    def is_valid_word(self, word):
        if word.upper() in self.file:
            return "Valid"
        else:
            return "Input not valid"

    def get_anagrams(self, word):
        word_list = list(word.upper())
        word_list.sort()
        anagram_list = []
        for item in self.file:
            item_list = list(item)
            item_list.sort()
            if item_list == word_list:
                anagram_list.append(item.lower())
        if len(anagram_list) == 0:
            return "None found."
        else:
            return anagram_list


# anagram1 = AnagramChecker()
# print(anagram1.is_valid_word("meat"))
# print(anagram1.get_anagrams("meat"))
