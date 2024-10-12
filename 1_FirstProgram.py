
#introduce yourself to Python 


print("Hello Python!! \n")

name=input("Python: Hi!, What is your name? \n")

print("Me: My name is " + name)
# Giving "+" at the end concatenates the string with variable output without spacebar

print("Python: Have fun learning :)", name)
# Giving " , " at the end seperates the string with variable output with spacebar


#This is how print fuction from official documentation look like,

# print(*object, sep=" ",end="\n", file=sys.stdout, flush=False)

# Here '*object' is the thing you type inside the function; 'sep' means seperator and 'end' means how its going to end, now here it is new line(\n), that means every at print(), the output comes on newline, you can manipulate this function's working by putting end="" or sep="" , so whenever you take output from a seperate print function it will print of the same line of preceding output for end and variable will attach to the string without spacebar.