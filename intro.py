"""
print("Hello Guys")

# this is just an example for an addition

print(40 + 50)

"""

#print("Hello World")


# Dynamic Lang :

# Name = "Monisha"


# Variables :

"""
    Variables are containers for storing data values.

    variable_name = value

"""

# Creating Variables  :


"""
age = 34

print(age)

print(age + 10)

print(age/4)

"""

# Variable Names are Case Sensitive :

"""
AgE = 40

Age = 30

"""

# Variable Names :

"""

- a variable name must start with a letter or the underscore character
- cannot start with a number
- can only contain aplha-numeric characters and underscores(A-z,0-9,_)
- cannot be any of the python keywords

ex :

    print =

    def =

    if =

    else =

    sum =

    list =

# Legal variable names :

useraddress = "Chennai"

user_address = "Chennai"

UserAddress = "Chennai"

useraddress13 = "Chennai"

_useraddress = "Chennai"


# illegal variable Names :

14useraddress = "Chennai"

user address = "Chennai"

user-address = "Chennai"

"""

# Multi words variable names :


#useraccountverificationpassword = "122345"

"""
Camel Case :

    Each word except the first,starts with a capital letter

        userAccountVerificationPassword = "122345"
    
Pascal Case

    Each word starts with capital letter

        UserAccountVerificationPassword = "122345"

Snake Case

    Each word separated by an undescore character

        user_account_verification_password = "122345"

"""


# print("Hello World");print("Welcome")

# ========== Data Types In Python ==========

"""

1. Numeric Data Type
2. Text Data Type
3. Sequence Data Type
4. Mapping Data Type
5. Set Data Type
6. Boolean Data Type
7. None Data Type
"""


# Numeric Data Type :


# Integer : int()

"""
    - Integer is a Whole Number
    - Positive or Negative
    - Without Decimals
    - Unlimited Length

    num = -2874298374387437 or 96489747
"""

# type()

"""
    age = 45

print(type(age))

"""

# Float : float()

"""
    - Floating Point Numbers
    - Positive or Negative
    - Withdecimals
    - Unlimited length
    - e --> Scientific Number [ e - power 10]

    num = -99.345 or 2329829849.2323232323232
"""

#salary = 45000.345678
#print(type(salary))

"""
BMI = 3e2

print(BMI)
print(type(BMI))

"""

# Complex : complex()

"""
    - Real + imaginary Number
    - 'J' as a Imaginary number
    - a + bj --> a real nuber + bj imaginary number

    - Complex Data type used for Scientific Applcations,Mathematical Based Application ,Electrical Engineering Based Applications
    - c , c++ ,java not having this data type python only have
"""

# Example : 

"""
#x = 3 + 4j

x = 4j + 6j
y = 3 + 4j

z = x + y

print(z)

print("Real : ",z.real," - Imaginary : ",z.imag)

print(type(z))

"""


#Boolean Data Type :

# Boolean : bool()

"""
    - It represents True or False

    Truthy Values :

        Any number is True, Except 0

        Any String is True, Except Empty String

        Any List ,tuple,set,Dictionary are True Except empty one
             
"""

#name = []

#print(bool(name))



# Text Data Type :

# String : str()


'''
name = 'varun45'

# Multiline String :

info = """varun is a Java DEveloper

and he is an trainer also and
he is working as an freelancer also
"""

print(info)
print(type(info))


'''

# Sequence Data Type :

# List :

"""
    fruits = ["Apple","Orange","Mango"]
"""


# Tuple :

"""
    numbers = (10,20,30,40,50)
"""

# range(1,10)





# Set Data Type :

# set()

"""
    names = {"Varun","ARun","Mani"}
"""

# Mapping Data Type :

# Dictionary : dict()

"""
    info = {"Name" : "Varun", "Age" : 24,"Address" : "Chennai"}
"""





# Input Field : input("Prompt")

"""
name = input("Enter your Name : ")

print(name)

print(type(name))

"""


# Type Casting :


num = "3asd45"

x = int(num)

print(x)
print(type(x))
















