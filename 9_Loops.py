# Loops: A loop is a sequence of instruction(s) that is continually repeated until a certain condition is reached. 

# _________________Types of Loops: ___________________

# While: A while loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition.
# Syntax: while 'Boolean expression'
#         ....block of codes ---
#         ....iteration

# --------Example---------

# i=0
# while i<3:
#     print("hello")
#     i+=1  #In Python you cannot use increment or decrement operator so we use compound assignmet operators.

# For: A "For" Loop is used to repeat a specific block of code a known number of times.
# * Syntax: for 'variable' in ([0,1,2,....,n]/range(n) -----> n= 0,1,2,3,....)
#        * ....block of codes ---
#         

# --------Example---------

# for i in [0,1,2]: #if you don't bother of variable while counting give ' _ ' 
#     print("Hello")
    
# OR
    
# for i in range(3):
#     print("Hello")

# By "Pythonic ways" you can perform for loop in a single line just using '*' after string 
# Syntax: print("xyz"*n) -----> n= 0,1,2,3,....

# --------Revised Example---------

# print("Hello\n"*3,end="")

# You can decide the magnitutde of the loop by accepting it from the user

# --------Example---------

# i=int(input("Enter count: "))

# for i in [0,1,2]:
#     print("Hello")
    
# OR
    
# for _ in range(i):
#     print("Hello")

# OR

# print("Hello\n" * i , end="" )

# Lists: A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.
# Syntax: variable=["abc","def",.........] # *Similar to array of strings in C programming 

# --------Example---------

# friends = ["Vaibhav","Dhanraj","Sumit","Samarth"]

# print("My Friends are: ")

# for a_friend in friends: # *Here you are using count variable to display the output so don't use ' _ ' here..
#     print(a_friend) 

# You also can iterate a list

# --------Example---------

# friends = ["Vaibhav","Dhanraj","Sumit","Samarth"]

# print("My Friends are: ")

# for f in range(len(friends)): 
#     print(friends[f]) 

# Here len() function gives integer lenght of list/string

# You can iterate multiple variables in a single for loop

# --------Example---------

# friends = ["Vaibhav","Dhanraj","Sumit","Samarth"]

# print("Friend list: ")

# for i in range(len(friends)): 
#     print(i+1, friends[i]) 

# Dictionaries (Dict):  Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and do not allow duplicates. It allows you to associate something with something else.
#Syntax:  **** variable =  {key1:val1, key2:val2, ....., keyN:valN} ****

# --------Example---------

# Friends= { 
#           "Samarth":"WIT", 
#           "Sumit":"WIT", 
#           "Ojas":"VIT", 
#           "Soham":"IIT Bombay"
#          } #You can arrange dictionaries by keeping each value below it

# print("Their college:")
# print(Friends["Samarth"])
# print(Friends["Sumit"])
# print(Friends["Ojas"])
# print(Friends["Soham"])


# You can print values more easily via loops
# When you use a for loop in Python to iterate over a dictionary, by design, it iterates over all of the keys.
# So we iterate the list with key being its index

# --------Example---------

# Colleges= { 
#           "Samarth":"WIT", 
#           "Sumit":"WIT", 
#           "Ojas":"VIT", 
#           "Soham":"IIT Bombay"
#          } 

# for a_friend in Colleges: # for (each value of) i in Friends, here i is the key, Friend[i] is the value 
#     print(a_friend+" studies in "+Colleges[i])

# You can take multiple key and value pairs at once
# Syntax: ****variable=[{key:value pairs 1},{key:value pairs 2},......]****

# --------Example---------

# Friends= [ 
#           {"name":"Samarth","college":"WIT","place":"Solapur"}, 
#           {"name":"Pranjal","college":None,"place":"Nepal"}, # 'None' is a keyword which represents no value to the key
#           {"name":"Ojas","college":"VIT","place":"Pune"}, 
#           {"name":"Soham","college":"IIT Bombay","place":"Mumbai"}, 
#          ]

# print("Name:  ",end="")
# for data in Friends: 
#     print(data["name"],end="  ")
    
# print("\nCollege:  ",end="")
# for data in Friends: 
#     print(data["college"],end="    ")
    
# print("\nPlace:  ",end="")
# for data in Friends: 
#     print(data["place"],end="   ")

# Nested Loops: Loops enclosed inside Loops are called nested loops.

# --------Example---------

# def main():
#     height=int(input("Enter Size of block: "))
#     print_block(height)
    

# def print_block(ht):
#     for i in range(ht):
#         for j in range(ht):
#             print("* ",end="")
#         print()

# OR

# def print_block(ht):
#     for i in range(ht):
#         print("* "* ht, end="")
#         print()


# main()