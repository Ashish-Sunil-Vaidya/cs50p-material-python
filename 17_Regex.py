# There are times we have to validate user input for ex: email , if user does not put @gmail or .com or domain name etc
# Creating logic with yourself is very inefficent and time consuming, for that a third party library was formed name  "re" it contains methods to regulate user input
# One of them is .search()

# @head 1) .search()

# @def .search() all notation

# @def ('.') -> all characters accepted except "\n"
# @def ('*') -> no or many repitions allowed
# @def ('+') -> 1 or many repitions allowed
# @def ('?') -> no or only one repetitions allowed
# @def ('{m}') -> m times repetitions allowed
# @def ('{m,n}') -> between m times and n times repetitions allowed
# @def ('^') -> starts checking where its applied
# @def ('$') -> stops checking where its applied
# @def ('[]') -> Set of characters inside the square brackets are accepted
# @def ('[^]') -> implies complementary set or anything accepted except the characters inside the brackets
# @def ('\w') -> word character covering alphanumeric characters and underscore
# @def ((...)) -> lists of combination
# @def (?: ...) -> exclude foll lists of combinations 
# @def ((A|B)) -> Imples either A or B to be selected

import re

while True:
    email = input("Enter Email -> ")
    if re.search(r"^\w+@\w+\.(com|gov|in)$",email):# @imp Here "r" means raw mode which tells the intepreter to read the data as a raw string which implies escape sequence characters
        print("Valid")
    elif email == "exit":
        exit(1)
    else:
        print("Not Valid")