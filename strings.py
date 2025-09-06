# Strings :

# name = '' or "" or """ """



# Strings are arrays :

x = "Hello-World-welcome"

# print(x[0])

# Find a length :

# print(len(x))


# String Modifications :

"""
lower() :

    convert to lowercase

upper() :

    convert to uppercase

strip()

    remove whitespace

split()

    split a string

replace()

    replace a value

"""

# Examples :

"""
print(x.lower())

print(x.upper())

print(x)

print(x.strip())

print(x.split("W"))

print(x.replace('welcome','Thank You'))

"""

# Concatenation :

"""
    we cannot combine strings & number
    Only strings are concatenate

"""
# Examples :

"""
x = "Varun"

y = "Welcome"

z = "hi"+ " " + x + " " + y + " " + "to Chennai."

print(z)

"""

#  Format Strings : format()

"""
 The format method takes unlimited number of arguments are passed in respective placeholders

"""

name = input("Enter Your name : ")

office = input("Enter Your office : ")

salary = int(input("Enter Your salary : "))


'''
txt = "hi my name is {2} ,i'm working in {0} and my salary is {1}"

print(txt.format(office,salary,name))

'''

# f-string :

txt = f"hi my name is {name} ,i'm working in {office} and my salary is {salary}"

print(txt)

