

# By default python inputs anything in form of string (str) because we input anything from keyboard and that is why it is in form of  'text'.
# So if you try to add two digits for example 1 and 2 it will not print 3 whereas it will print 12

# ----------Example----------

# x=input("Enter X: ")
# y=input("Enter y: ")

# z=x+y # You can also directly do addition by placing x+y in print() now here it is for sake of learning, dont waste memory for a variable which is going to be used only once.  

# print(f"Sum = {z}") # In python plus is for concatenation of string that is why it shows two inputs together 

# In order to do mathematical calculation you first have to convert this string into integer or float it can be done in following ways: 

# ----------Example----------

# x=input("Enter X: ")
# y=input("Enter y: ")
# print(f"Sum = {int(x)+int(y)}") 

# # OR

# x=int(input("Enter X: "))
# y=int(input("Enter y: "))
# print(f"Sum = {x+y}")

# OR

# print( int(input("Enter X: ")) + int(input("Enter y: ")))

# Here we typecasted input aswell as output to get mathematical output here "int" is a function

# We can also do the above things to float aswell..

# ----------Example----------

# x=input("Enter X: ")
# y=input("Enter y: ")
# print(f"Sum = {float(x)+float(y)}") 

# # OR

# x=float(input("Enter X: "))
# y=float(input("Enter y: "))
# print(f"Sum = {x+y}")

# OR

# print( float(input("Enter X: ")) + float(input("Enter y: ")))

# Round Function: Sometimes user does not need a accurate decimal values but a nearest integer to the floating value, then we have to use round function.

#* Syntax: round(number/variables,[nth decimal])  here anything optional inside function in programming is shown in square brackets ' [] '.

# ----------Example----------

# x=float(input("Enter X: "))
# y=float(input("Enter y: "))
# z=round(x+y)
# print(f"Sum = {z}")

# ----------Example----------

# x=float(input("Enter X: "))
# y=float(input("Enter y: "))
# z=round(x/y,2)
# print(f"Division = {z}")

# OR

# x=float(input("Enter X: "))
# y=float(input("Enter y: "))
# print(f"Division = {round(x/y,2)}")

# OR

# x=float(input("Enter X: "))
# y=float(input("Enter y: "))
# print(f"Division = {x/y:.2f}") #We have used (.nf) to round upto n decimals in C programming

# You can add comma to greater values make it understandable at which tense place is the number i.e '1,000' instead of 1000

# Syntax: **** varibiable:, **** 

# ----------Example----------

# x=int(input("Enter X: "))
# y=int(input("Enter y: "))
# print(f"Sum = {x+y:,}")