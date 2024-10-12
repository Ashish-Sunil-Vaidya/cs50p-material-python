# Functions: A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

# --------Example---------

# def greet(to="World"):   #Fuction Definition: You can define a funcion to perform your given task so we can use it later in a line by calling it
#     print("Hello,",to)

# greet() #Fuction call: You request the function to peform the task.
# name=input("What is your name? ")
# greet(name)

# Here it looks good for a single line code but if you are writing many functions you are indirectly coding in reverse order, Let's define a function below to its call, it will not detect the function as the compiler always runs code from top to bottom, as the function is not defined at top it will give error telling function does not exist, so in order to solve this problem we define our codes outside function as, def main() then define the function and then main() call.


# --------Example---------

# def main():
#     name=input("What is your name? ")
#     greet(name)
#     greet()  #Function without arguments prints the default value of parameter inside definition
    
# def greet(to="World"):
#     print("Hello,",to)

# main() # We call main at last because the all the lines of user function will be scanned and print the output accordingly

#Note: Do not add variable declared inside main function in defined function as it will not detect it as a argument also in other words the variable not present inside that 'scope' .

# You can return a value from a function by using return
# Syntax:  **** return 'variable' ****

# --------Example---------


# def main():
#     x=int(input("Enter number to be squared:"))
#     print(f"Square of {x} is {square(x)}")

# def square(n):
#     return n*n # Or n**2 Or pow(n,2) Here '**' operator gives power to a variable
    
# main()