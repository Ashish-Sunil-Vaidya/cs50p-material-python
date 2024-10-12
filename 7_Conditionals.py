#Conditionals/Control flow statements:  Conditionals in python are just like in C we compare two or more things and get values in 0 or 1, here 0 represents false and 1 represents true, here we make use of relational opertors i.e. (>=,<=,==,>,<,!=) 

# if : This is a keyword which compares one variable to another and if true it displays the output inside its block 
# *Syntax:  if/elif 'expression':
# *          . . . .Block of codes
# --------Example---------

# x=int(input("Enter x:"))
# y=int(input("Enter y:"))

# if x>y: #'if' asks question to the compiler, 'if' is true prints the answer ,if false it doesn't and other if is present, it asks question to the other if
#     print("x is greater than y")

# elif x<y: # it only asks question if the preceeding condition becomes false, incase of 'if' even it is true it will ask question to other if,using 'if - elif' ladder makes program faster than 'if' ladder.
#     print("x is less than y")

# else:  #if none of the conditions are true without asking questions, without checking the condition it will consider 'else' statment as true.
#     print("x is equal y")
    
# # Proper combination of if-elif-else will not only make your codes readable, also it will slightly improve performance of the program  



# 'Or' conditionals:       In English 'Or' is a conjunction which joins two or more sentences together, same goes in python or any other programming language but with slight difference, it not only joins two or more boolean expressions together and performs OR logic operation on these boolean expression, if one of the statements in OR is true, whole condition becomes true just like OR gate.

#* Syntax:  if/elif 'expression1' or 'expression2' or 'expressionN':
# *         . . . .Block of codes


# --------Example---------

# x=int(input("Enter x:"))
# y=int(input("Enter y:"))

# if x<y or x>y:
#     print("x is not equal to y")

# else:
#     print("x is equal y")

# Note: Above examples were for the sake of learning, use common sense while creating conditional statements based on your requirements, this will make your conditional codes more readable and more effiencient. 
# Take above example, why to prove if x<y and x>y for proving its unequal, instead we can use '!=' relational operator to prove if its equal or unequal.

# --------Revised Example---------

# x=int(input("Enter x:"))
# y=int(input("Enter y:"))

# if x!=y:
#     print("x is not equal to y")

# else:
#     print("x is equal y")

# This looks more readable and it does not go from unwanted extra conditions, so program becomes faster than before.

# 'And' conditionals: In English, just like 'Or' , 'And' is also a conjunction which joins two or more sentences together, it joins two or more boolean expressions together and performs AND logic operation on these boolean expression, if one of the statements in AND is false, whole condition becomes false just like AND gate. 
# This conditional is mostly used to prove if value belongs in the group or not like grading in school, if you score between 95 to 100 you get 'A+', 94 to 90 'A' and so on.

# --------Example---------

# score=int(input("Enter your score: "))

# if score>=95 and score<=100:
#     print("Grade: A+")
# elif score>=90 and score<95:
#     print("Grade: A")
# elif score>=80 and score<90:
#     print("Grade: B")
# elif score>=65 and score<80:
#     print("Grade: C")
# elif score>=35 and score<65:
#     print("Grade: D")
# else: 
#     print("Fail")
    
# instead of x>50 and x<100, just like in mathematics you can write in following way :   50<x<100, this feature is availble in python not in other languages like C,C++ or Java.

# --------Revised Example---------

# score=int(input("Enter your score: "))

# if 95<=score<=100:
#     print("Grade: A+")
# elif 90<score<=95:
#     print("Grade: A")
# elif 80<score<=90:
#     print("Grade: B")
# elif 65<score<=80:
#     print("Grade: C")
# elif 35<score<=65:
#     print("Grade: D")
# else: 
#     print("Fail")


# Here in above examples lets think more logically, instead of asking same two questions of greater than or less tha every time, we can use a single question to every statement to make program readable and less chances to bugs by other programmers.
# --------Revised Example---------

# score=int(input("Enter your score: "))

# if score>=95:
#     print("Grade: A+")
# elif score>=90:
#     print("Grade: A")
# elif score>=80:
#     print("Grade: B")
# elif score>=65:
#     print("Grade: C")
# elif score>=35:
#     print("Grade: D")
# else: 
#     print("Fail")
    
# Here condition checks if the score is near to condition's score, example 95 here 95 is near to condition score>=95 hence,it will print the Grade: A+, if less than 95 it will printf Grade: B, and so on...

# Match:  Match is just 'switch-case' of python, it is just like if-else but more compact and more effecient in large numbers than it.
#* Syntax:  Match 'variable' :
#*          ....case 1:
#*              ....block of statments
#*          ....case 2:
#*              ....block of statments
#*              ....

# --------Example---------

# n=int(input("Enter number: "))

# match n:
#     case 1:
#         print("one")
#     case 2:
#         print("two")
#     case 3:
#         print("three")
#     case _:
#         print("Greater than three")
        