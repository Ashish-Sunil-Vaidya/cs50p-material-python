# Presently, most frequent way of displaying output of a variable is 
 
# print("Hello Python!! \n")
# name=input("Python: Hi!, What is your name? \n")
# print("Me: My name is {name}" )
# print(f"Python: Have fun learning :) {name}")

#Here 'f' tells the compiler that this string is using something special called 'format string' and due to this '{VariableName}' acts like a format specifier just like in C programming(%d,%f,etc), if you dont use 'f' at first, it will show {VariableName} in output instead of inputted value like a normal string

# __________________________________________________________________METHODS___________________________________________________________________

# Methods: In object-oriented programming, a method is a programmed procedure that is defined as part of a class and included in any object of that class.
# Methods are functions.
#If you give many whitespaces before or after the string while inputting, by default it will also print the whitespaces in the output. like if you input "      abcd    " it will print "      abcd    " in output
# For user convienience and for better grammar for user you can remove these unrequired whitespaces by using ".strip()" method

# **** Syntax: variable=variable.strip() **** 

#---------Example--------
# print("Hello Python!! \n")
# name=input("Python: Hi!, What is your name? \n")
# name=name.strip()
# print(f"Me: My name is {name}" )
# print(f"Python: Have fun learning :) {name}")

# Most of the times while inputting Names/Full names for example user does not input their names capitalised, you can add some convenience by using method called ".capitalize()"

# **** Syntax: variable=variable.capitalize() **** 

#---------Example--------
# print("Hello Python!! \n")
# name=input("Python: Hi!, What is your full name?\n")# ashish vaidya
# name=name.capitalize() #Ashish vaidya
# print(f"Me: My name is {name}" )
# print(f"Python: Have fun learning :) {name}")

# The ".capitalize" method capitalizes only the first word, so if you take full name from user like: First name , middle name and surname;  the middle name and surname will not capitalize, if you want every single word to be capitalized we used another method called ".title"

# **** Syntax: variable=variable.title() **** 

#---------Example--------
# print("Hello Python!! \n")
# name=input("Python: Hi!, What is your full name?\n")# ashish vaidya
# name=name.title() #Ashish Vaidya
# print(f"Me: My name is {name}" )
# print(f"Python: Have fun learning :) {name}")

# You can chain multiple methods for more customization to your output
# ****Syntax: variable = variable.method1().method2().method3(). ... .methodN()****

#---------Example--------
# print("Hello Python!! \n")
# name=input("Python: Hi!, What is your full name?\n")#             [Whitespaces]                 ashish vaidya
# name=name.title().strip() #Ashish Vaidya
# print(f"Me: My name is {name}" )
# print(f"Python: Have fun learning :) {name}")

# You can make it more readable by adding .methods after input function, it makes it easier to customize and reduces writing codes

#---------Example--------
# print("Hello Python!! \n")
# name=input("Python: Hi!, What is your full name?\n").title().strip() 
# print(f"Me: My name is {name}" )
# print(f"Python: Have fun learning :) {name}")

# At some stage the above methods will also cause problems in readability, when it becomes a very very long line, so both methods come with pros and cons. This is company and team dependent issue, some might like the first one while others the second, if you are working in a industry you have to use any of the above assigned by the company heads.

# You can split a full name into seperate strings or ingeneral any strings into n seperate strings in n number of variables. For this we use the method (.split('what is the key thing for spliting'))
# ****Syntax: variable1,varible2,......,variableN = variable.split **** 
# 
# #---------Example--------
# print("Hello Python!! \n")
# name=input("Python: Hi!, What is your full name?\n")
# first,middle,last = name.split(" ") 
# print(f"Me: My First name is {first}" )
# print(f"Me: My Middle name is {middle}" )
# print(f"Me: My Last name is {last}" )
# print(f"Python: Have fun learning :) {name}")               