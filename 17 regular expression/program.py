# A Regular Expression or RegEx is a special sequence of characters that uses a search pattern to find a string or
# set of strings.
# It can detect the presence or absence of a text by matching it with a particular pattern and also can split a pattern into one
# or more sub pattern.

#  re -re is the library 

#  match()
import re

result = re.match("Hatake", "Hi, My Name is Kakashi Hatake.")
print(result)

result = re.match("Hi", "Hi, My Name is Kakashi Hatake.")
print(result)

# search()

result = re.search("Duniya", "Namaste Duniya !")
print(result)

# findall
result = re.findall(r"\d+","There are 3 dogs and 4 cats.")  # \d+ matches one or more numbers (0-9)
print(result)

# sub() - Replaces all occurrences of a pattern with a specified string 
result = re.sub(r"\d+", "@", "There are 3 dogs and 4 cats")
print(result)


# \d matches a single digit (0-9) 
# \d+ matches one or more digits 
# \s matches any whitespace character

