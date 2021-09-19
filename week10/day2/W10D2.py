import re

string = "at what time?"
match = re.findall('at', string)
print(match)

string = "at what time?"
match = re.search('of', string)
if match:
    print("String found at: ", match.start())
else:
    print("String not found!")

string = "at what time?"
match = re.split('a', string)
print(match)

string = "at what time?"
match = re.sub("\s", "!!!", string)
print(match)
