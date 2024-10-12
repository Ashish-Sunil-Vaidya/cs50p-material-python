# Exceptions: An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions.
# This can be dangerous at Industry level as a hacker or any malacious user can manipulate your program or crash it using these error issues.
# We can avoid such issues in python by using by 'try-except'
# Synatx: try:
#         ....block of codes

#         except (type of error):
#         ....message to convey it to user after execution

# --------Error Example---------

# x=int(input("Enter integer: "))
# print(f"Integer is {x}") #If you input a string here we get "ValueError: invalid literal for int() with base 10: 'cat' " 

# We can avoid this error mesage by following way

# --------Revised Example 1---------

# try:
#     x=int(input("Enter integer: "))  
#     print(f"Integer is {x}") 
    
# except ValueError:
#     print("Your input not a integer")

# Inorder make the program more readable we tend to take print() out of try-except but, an issue occurs if you input wrong value, it will give new kind of error called as 'NameError'. This error means there is no assignment of value inside the variable i.e. the variable has no values. We can fix this by making print() mutually exclusive by adding else to the output statment. 

# --------Revised Example 2---------

# try:
#     x=int(input("Enter integer: "))  
    
# except ValueError:
#     print("Your input not a integer")
    
# else:
#     print(f"Integer is {x}") 

# You can also use loops inside for try-execption, its a good practice to ask input again if they input wrong values.

# --------Revised Example 3---------
# while True:
#     try:
#         x=int(input("Enter integer: "))  
    
#     except ValueError:
#         print("Your input not a integer")
    
#     else: break
    
# print(f"Integer is {x}") 

# OR

# while True:
#     try:
#         x=int(input("Enter integer: "))  # Here if you do error in input it directly shifts to 'execpt' function without taking care of block of codes below it.
#         break # So it breaks when the value is a integer 
    
#     except ValueError:
#         print("Your input not a integer")
    
# print(f"Integer is {x}") 

# You can also use 'try-execpt' with fuctions and can also be shared with others

# --------Example---------


# def main():
#     x=is_int()
#     print(f"Integer is {x}")

# def is_int():
#     while True:
#         try:
#             x=int(input("Enter integer: "))
            
#         except ValueError:
#             print("Your input not a integer")
            
#         else: break
        
#     return x
    
# main()

# OR

# def main():
#     x=is_int()
#     print(f"Integer is {x}")

# def is_int():
#     while True:
#         try:
#             x=int(input("Enter integer: "))
#             return x # Return does both the job of breaking and returning the value of function
            
#         except ValueError:
#             print("Your input not a integer")
        
# main()

# OR

# def main():
#     x=is_int()
#     print(f"Integer is {x}")

# def is_int():
#     while True:
#         try:   
#             return int(input("Enter integer: "))
            
#         except ValueError:
#             print("Your input not a integer")
        
# main()

# Pass: The pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
# Synatax : pass

# --------Example---------

# def main():
#     x=is_int()
#     print(f"Integer is {x}")

# def is_int():
#     while True:
#         try:   
#             return int(input("Enter integer: "))
            
#         except ValueError:
#             pass
        
# main()

# Prompt: To receive information through the keyboard, Python uses the input() function. This function has an optional parameter, commonly known as prompt, which is a string that will be printed on the screen whenever the function is called.
# Synatx: PROMPT 

# --------Example---------

# from cmd import PROMPT


# def main():
#     x=is_int("Enter Integer: ")
#     print(f"Integer is {x}")

# def is_int(PROMPT):
#     while True:
#         try:   
#             return int(input(PROMPT))
            
#         except ValueError:
#             pass
        
# main()