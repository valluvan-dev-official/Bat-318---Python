# Function :

"""
What are Python Functions?

A function is a block of organized, reusable code designed to perform a specific task. Functions allow for better modularity and code reuse in Python.

- set of instructions called as a function
- a reusable block of code that performs a specific task or set of tasks.


Types of functions :

    1. built-in Functions
    2. user-defined Functions
    3. lambda Functions

Built-in Functions :

    print()
    len()
    copy()
    append()
    list()
    update()
    enumerate()


User Defined Functions :

    There are two types of concepts:

        1. Void Functions     - it returns nothing

            1. With Arguments
            2. Without Arguments

        2. Non-void Functions - it has something to return

            1. With Arguments
            2. Without Arguments


Syntax :

def function_name(parameters):
    code to be executed

    
def - keyword for declare a function

function_name - name of the function

parameters - optional, it is a variable that is passed to the function

"""

# Void Function :


# Without Argument :

"""
def myfun():

    a = 10

    b = 20

    c = a + b

    print(" a -- ",a)
    print(" b -- ",b)

    print(" Addition of a + b is = ",c)


print(myfun())

"""

# With Argument :


"""
def myfun(a,b):

    c = a + b 

    print("C is -- ",c)



x = int(input("Enter num : "))

y = int(input("Enter num : "))


myfun(20,30)

print(myfun(x,y))

myfun(100,200)

"""


# Non Void :

# without argument :

"""
def myfun():

    a = 10

    b = 30

    c = a + b 

    return c


print(myfun())

"""

# With Argument :

"""
def Myfun(x,y):

    num = x + y 

    return num


a = 30

b = 3

print(Myfun(a,b))

"""


# ========= Returning Multiple Values : ===========


"""
def calculate(a,b):

    addition = a + b

    subtraction = a - b 

    Multiply = a * b 

    return addition,subtraction,Multiply


print(calculate(20,5))

add_,sub_,mul_ = calculate(20,5) # (25,25,100)


print(add_)
print(sub_)
print(mul_)



"""














































