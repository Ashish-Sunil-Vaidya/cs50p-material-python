# Unit test are tests which are performed to check whether your code has bugs, if there are bugs it will give you error
# If we choose to test anything if would multiple lines of if else statments that will make your code unreadable
# Python introduced a keyword called  "assert" which tests your code automatically reducing time taken

# @def Syntax: assert function_name(test_args, ... ) == required_value   
# There is one big problem in "assert", it only shows the line where error occured but not the explanation , i.e. it will find where is the error but not tell why did it occured
# ! Traceback (most recent call last):
# !   File "e:\Programming\Python\Problems\testimport.py", line 7, in <module>
# !     main()
# !   File "e:\Programming\Python\Problems\testimport.py", line 4, in main
# !     assert add(10,20) == 40
# ! AssertionError
# For that some programmers created third party libraries to make assert useful
# Example: Pytest - It shows error line with visual representation of value within the test case

# @def Syntax(in terminal): pytest *test*filename.py

# @imp It is convenient to write code of different functionality in unique function, as it not only makes it readable but also it makes testing easier, while performing tests it is required to return value of the function 

# @imp You can run collection of unit tests at once by creating packages, A package is folder of python files. To create a package simply just create a filename called "__init__.py" it will automatically create a package of the existing folder