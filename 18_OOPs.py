# In python we can return multiple values by creating lists, dictonary or #* Tuple
# Tuple is a immutable list, it is used to return two or more values from a function

# def main():
#     stud_data = getDetails();
#     print(f"Name: {stud_data[0]} Age: {stud_data[1]} RollNo: {stud_data[2]}")

# def getDetails():
#     name = input("Input Name -> ");
#     age = input("Input Age -> ");
#     rollno = input("Input Roll No -> ");
#     return (name,age,rollno); #Returning a tuple here you cannot overwrite the data inside tuple

# main()

# ? OR

# def main():
#     stud_data = getDetails();
#     print(f"Name: {stud_data[0]} Age: {stud_data[1]} RollNo: {stud_data[2]}")

# def getDetails():
#     name = input("Input Name -> ");
#     age = input("Input Age -> ");
#     rollno = input("Input Roll No -> ");
#     return [name,age,rollno]; #Returning a list here you can overwrite the data inside as it is a list

# if __name__ == "__main__":
#     main()

# ? OR


# def main():
#     stud_data = getDetails()
#     print(f"Name: {stud_data['name']} Age: {stud_data['age']} RollNo: {stud_data['rollno']}")


# def getDetails():
#     student = {}
#     student["name"] = input("Input Name -> ");
#     student["age"] = input("Input Age -> ");
#     student["rollno"] = input("Input Roll No -> ");
#     return student; #* Returning a dictonary here you can make code readable by keys while accesing index

#     name = input("Input Name -> ");
#     age = input("Input Age -> ");
#     rollno = input("Input Roll No -> ");
#     return {"name": name ,"age": age, "rollno": rollno}  #* Returning a dictonary here you can make code readable by keys while accesing index
#

# if __name__ == "__main__":
#     main()


# @head                Object Oriented Programmming

# @def:   Object-Oriented Programming is a methodology or paradigm to design a program using classes and objects.

# @def:   Class: In object-oriented programming, a class is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined objects are created using the class keyword.

# @def:   Objects: In object-oriented programming (OOP), objects are the things you think about first in designing a program and they are also the units of code that are eventually derived from the process.

# * Example

# class Student:
#     ...

# def main():
#     stud = getDetails();
#     print(f"Name: {stud.name}\n Age: {stud.age} \nRollNo: {stud.rollno}")

# def getDetails():
#     student = Student();
#     student.name = input("Input Name -> ");
#     student.age = input("Input Age -> ");
#     student.rollno = input("Input Roll No -> ");
#     return student; #Returning a object

# main()

# ?                   OR

# class Student:
# *      Intializing an object using constructor __init__
#     def __init__(this,name,age,rollno): #@imp  use " self " instead of this, it is just to show its similar to OOps like java python
#         this.name = name;
#         this.age = age;
#         this.rollno = rollno;


# def main():
#     stud = getDetails();
#     print(f"Name: {stud.name}\nAge: {stud.age}\nRollNo: {stud.rollno}")

# def getDetails():
#     name = input("Input Name -> ");
#     age = input("Input Age -> ");
#     rollno = input("Input Roll No -> ");
#     student = Student(name,age,rollno);
#     return student; #Returning a object

# main()
