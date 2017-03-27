import math

# To Add a support for a new operation
# Write the appropriate function here
# and add it in the _OpKeyWords dictionary with a suitable priority
# and suitable keywords
# also add a rule set in _OpRuleSets 

# for special rules add an extra elif condition in parse method
# however it is highly discouraged
    
def add(arg0, arg1):
    return arg0 + arg1

def add(arg0, arg1):
    return arg0 + arg1

def subtract(arg0, arg1):
    return arg0 - arg1

def multiply(arg0, arg1):
    return arg0 * arg1

def divide(arg0, arg1):
    return arg0 / arg1

def power(arg0, arg1):
    return pow(arg0, arg1)

def square(arg0):
    return pow(arg0, 2)

def factorial(arg0):
    return math.factorial(arg0)

def sqrt(arg0):
    return math.sqrt(arg0)

def cube(arg0):
    return pow(arg0, 3)

def cube_root(arg0):
    return pow(arg0, 1/3)

def pi():
    return math.pi

def e():
    return math.e
