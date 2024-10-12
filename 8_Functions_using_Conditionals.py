# Conditionals can also be used inside functions, here we return values in form of new datatype called bool, bool only has 2 values 'True' or 'False'.Here the function is called in 'if' condition, if 'True' it will print block of codes below 'if' condition, if 'False' it prints block of codes below 'else' condition.

# --------Example---------

# def main():
#     num=int(input("Enter a number: "))
#     if is_even(num):
#         print(f"Number {num} is even")

#     else:
#         print(f"Number {num} is odd")


# def is_even(n):
#      if(n%2==0):
#          return True

#      else:
#          return False

# main()

#  Python has unique feature called 'pythonic expression' for making code simpler to be seen, here you can return value in single line by returning
# return if n%2==0 True else False

# But it can be refined more further, here instead of asking if-else question, the expression n%2==0 itself is a boolean equation so we can directly return this boolean equation instead of all if-else code.

# --------Revised Example---------

# def main():
#     num=int(input("Enter a number: "))
#     if is_even(num):
#         print(f"Number {num} is even")

#     else:
#         print(f"Number {num} is odd")


# def is_even(n):
#     return n%2==0

# main()

# this program is better than previous one as it is more readable than previous one.
