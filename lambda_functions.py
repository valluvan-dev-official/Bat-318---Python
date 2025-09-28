# Lambda Functions :

"""
A lambda function is a small anonymous function.
Used for short, single-expression functions.

Syntax :

    lambda arguments : expression


lambda: Keyword to define a lambda function.

arguments: Variables that are passed to the function.

expression: A single expression that is evaluated and returned by the lambda
    function.
"""


# square = lambda x : x * x 

# print(square(10))

"""

mul = lambda a : a * 2

print(mul(10))

"""


# =======================

# Lambda using Map()

# Syntax :

"""
map(function,iterables)

"""


# numbers = [2,3,4,5]

# multiply_2 = list(map(lambda x : 2 * x,numbers)) # 2 - 4, 

# print(multiply_2)



# using usr defined functions :

"""
def square(x):

    return x * x 


result = map(square,numbers)

print(list(result))

"""

# using lambda :

"""
result = map(lambda x : x * x,numbers)

print(list(result))

"""

# ======== Filter : ======


"""
Syntax :

    filter(function,iterable)
    
    function -> True are False Return pannum

        True return panna -> Element include aagum
        False return panna -> Element remove aagum


    function = None,Truthy Elements  

    None - Remove All Falsy Values

    Truthy Elements :

        - Elements that are considered True in a boolean context
        - Examples: Non-empty strings, non-zero numbers, non-empty lists, etc.

    Falsy Elements:

        - Elements that are considered False in a boolean context
        - Examples: Empty strings, zero, None, empty lists, etc.

        0
        0.0
        ""
        []
        ()
        {}
        None
        False


"""

# Example :

"""
numbers = [10,15,20,25,30,35]

even_numbers = filter(lambda x : x % 2 == 0, numbers ) # 10,20,30

print(list(even_numbers))

"""

# Example - 2

"""
words = ["Hi",""," ","Welcome","to","","Python"]

result = filter(None,words)

print(list(result))

"""

# Reduce :

from functools import reduce

# syntax :

"""

reduce(function,iterable,initializer)

reduce(lambda acc,current : acc + cur)
"""

# numbers = [1,2,3,4]

# total = reduce(lambda a,b : a + b ,numbers) 

"""
==> 0 + 1 = 1

a = 1

==> 1 + 2 = 3

a = 3

==> 3 + 3 = 6

a = 6

==> 6 + 4 = 10

"""

# print(total)


# ============= Lambda function for sorting =============

# Syntax :

# sorted(iterable,key = ...)

"""
iterable -> list,tuple,dict

key -> 
"""

# students = [("harish","Has",23),("monisha","Abs",18),("aravind","Zev",30),("varun","Per",27),("malar","Nope",20)]

# sort by age:


# sorted_students = sorted(students,key=lambda x : x[2]) 

"""
x = ("harish", 23)

x[1] = 23

"""

# print(sorted_students)



#  ============= Conditional Expression in Lambda ============

"""
Syntax :

    lambda arguments : value_if_True if condition else value if_False
"""

# Check even or Odd :

result = lambda x : "Even" if x % 2 == 0 else "Odd"

num = int(input("Enter a Num : "))

print(result(num))