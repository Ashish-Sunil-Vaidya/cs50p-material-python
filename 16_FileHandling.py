# File Handling/File I/O in Python is just like other programming languages but much simpler than other languages
# @def Syntax: file = open("filename.txt","mode") [modes are same as c, c++, java]  to open th file;


# @head Write mode in File

# name = input("Enter Name -> ")
# file = open("Names.txt","w")
# file.write(name)
# file.close()

# @imp Note: In write mode the everytime you run the program the older data is written with current input data, if you want to keep the other data as well you will have to append older data with current data, for that there is append mode

# @head Append mode in File

# name = input("Enter Name -> ")
# file = open("Names.txt","a")
# file.write(name) # *Appending bascially means you are cocatenating data one after the other
# file.write(f"{name}\n") # *This will make output look much readable
# file.close()


# @head Read mode in File

# file = open("Names.txt", "r")
# lines = file.readlines()
# for line in lines:
# print(f"{line}") # * The program gives following output

# ! Ashish print '\n'
# ! file '\n'
# ! Samarth print '\n'
# ! file '\n'
# ! Sumit print '\n'
# ! file '\n'

# This will not look great, in order to remove extra blanklines, it can be done in following ways
# 1. By formatting print(): # @def Syntax: print(f"Output" end="") (removes \n from print())
# 2. By using .rstrip() method # @def Syntax: readlines_variable.rstrip() (removes \n from file)
# for line in lines:
# print(f"{line}", end="")
# OR
# print(f"{line.rstrip()}")

# @head Reading Files  (Pythonic Ways)

# Sometimes programmers forget to close the file, this may lead to bugs or corruption of file
# with open("Names.txt") as file:
#     for line in lines:
#         print(f"{line}", end="")


# There are times programmer has to read different types of values for a single entity like lists and dictonary, it will be hard to differentiate values by line by line
# For such situation you can create a .csv file or comma separated values file


# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"Name: {row[0]} , Age: {row[1]} , Place: {row[2]}") # * Here split method converts row variable into a list and can be accessed via index iterator

# If you are sure in how many parts the string is going to split then you can assign different variable names to the splitted values

# with open("students.csv") as file:
#     for line in file:
#         name,age,location = line.rstrip().split(",")
#         print(f"Name: {name} , Age: {age} , Place: {location}") # @imp Note: splitted valued are assigned in order of variable names


# Consider you are sorting the data in terms of Name or Age, it is not posssible to sort data using above list method there might be conditions where Name would be first, at that situation it is an exception but not most of the time

# In order to sort data by values you have to use dictionary

# Implementing above program version in dictionary
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, age, location = line.rstrip().split(",")
# student = {}
# student["name"] = name
# student["age"] = age
# student["location"] = location
# students.append(student)
# OR
# student ={"name":name , "age":age, "location":location} # * Pythonic ways of declaration
# students.append(student)

# for student in students:
#         print(f"Name: {student['name']} , Age: {student['age']} , Place: {student['location']}")

# Now for sorting in terms of key or value we are going to define another function  whose sole purpose is going to be passed as argument assigning the key value # @def Syntax: sorted(dict_varname , key = function_name, reverse = T/F {reverse is optional if you want to sort in descending order})

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, age, location = line.rstrip().split(",")
#         student = {
#             "name": name,
#             "age": age,
#             "location": location,
#         }  # * Pythonic ways of declaration
#         students.append(student)


# def get_Name(student):
#     return student["name"]

# for student in sorted(students,key=get_Name , reverse=True):
#     print(
#         f"Name: {student['name']} , Age: {student['age']} , Place: {student['location']}"
#     )

# Instead of wasting lines of code we can use anonynous function called as lambda function instead of declaring function
# @def Syntax: sorted(dict_varname , key = lambda dict_name: dict_name["key"])

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, age, location = line.rstrip().split(",")
#         student = {
#             "name": name,
#             "age": age,
#             "location": location,
#         }  # * Pythonic ways of declaration
#         students.append(student)

# for student in sorted(students,key=lambda student: student["name"] , reverse=True):
#     print(
#         f"Name: {student['name']} , Age: {student['age']} , Place: {student['location']}"
#     )

# Somtimes in data when there is adress for example there is always a possibilty of having comma in address, it will spilt in differnt lists and cause more values than keys causing value unpack error.
# Not only comma it might be any seperating special symbol or logic
# Inorder to eliminate this isssue a library was created called "csv" to automate this process of splitting

# import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for Name, Age, Location in reader:  # Or just directly put csv.reader
#         students.append(
#             {
#                 "name": Name,
#                 "age": Age,
#                 "location": Location,
#             }
#             #Or creating student dictionary
#         )

# for student in sorted(students, key=lambda student: student["name"]):
#     print(
#         f"Name: {student['name']} , Age: {student['age']} , Place: {student['location']}"
#     )

# Everything we did was to make data readable but its not flexible nor robust if you change data or flip headings of data it will break the program
# To solve this issue there is difernt type of reader called as DictReader which returns dictonary rather than lists in previous code

# import csv

# students = []

# with open("students.csv") as file:

#     for row in csv.DictReader(file):
#         students.append(row)

# for student in sorted(students, key=lambda student: student["Name"]):
#     print(
#         f"Name: {student['Name']} , Age: {student['Age']} , Place: {student['Location']}"
#     )

# For adding data we do the following

# Using List method

# name = input("What's your name? -> ")
# age = int(input("What is your age? -> "))
# location = input("Adresss -> ")
# with open("students.csv","a") as file:
#     csv.writer(file).writerow([name,age,location])

# Using Dictionary method

# name = input("What's your name? -> ")
# age = int(input("What is your age? -> "))
# location = input("Adresss -> ")
# with open("students.csv","a") as file:
#     csv.DictWriter(file,fieldnames=["name","age","location"]).writerow({"name":name,"age":age,"location":location})
# # * Here in DictWriter, fieldnames make sure to read data and put in order w. r. t. key


# @head File Handling on Binary Files(Images,GIFS,Videos,Audio,etc)

# Above File operations we did in text files now we are going to manipulate image files and convert it into a GIF
# For doing file handling on images we have to import a library called pillow, Pillow helps us by giving us tools to mainpulate image type files

# import sys

# from PIL import Image


# images = []

# for arg in sys.argv[1:]:
#     image = Image.open(arg)
#     images.append(image)

# images[0].save(
#     "loading.gif", save_all=True, loop=0, append_images=[images[1]], duration=200
# )
