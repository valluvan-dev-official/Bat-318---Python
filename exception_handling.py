

"""
try:

    a = int(input("Enter a : "))

    print(a)

    print(23)

except:

    print("have some error we will connect you once the error cleared")

"""



"""
try:

    a = 20 

    b = int(input("Enter b : ")) 

    c = a / b 

    print(c)

except ZeroDivisionError:

    print("Not divisible by zero")

except:
    print("Welcome")

"""

# Using Else and Finally :

"""
try :

    num = int(input("Enter a number : "))

    total = 20 / num

except:
    print("Have some Error")

else:

    print(total)

finally :

    print("Thank You For Comming..")

"""


# Catching All Exceptions :

"""
try : 

    print(10/-2)

except Exception  as e:

    print("Error : - ",e)

"""

# Raise Exception Manually :

"""
num = int(input("Positive Number : "))


if num < 0:

    raise ValueError("Negative numbers are not allowed")

"""


# 


errors = dir(locals()['__builtins__'])

print(len(errors))

print(errors)