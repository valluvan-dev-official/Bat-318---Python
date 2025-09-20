
# conditional statements :

"""
Conditional statements are fundamental in Python for decision-making in programs. They allow the execution of certain blocks of code based on specific conditions. The key conditional statements in Python are if, if-else, if-elif-else, and nested if. These statements use boolean expressions to evaluate whether a condition is True or False.


Types of Conditional Statements

1. if Statement

The if statement executes a block of code only if the condition evaluates to True.

syntax :

    if condition:
        # Code to execute if the condition is True


"""

# ex :

"""
a = 1

if a > 10:

    print("a is greaterthan 10")


if a < 10:

    print("a is lessthan 10")

"""

# 2. if-else Statement

"""
The if-else statement provides an alternative block of code to execute when the condition is False.

syntax :

if condition:
    # Code to execute if the condition is True
else:
    # Code to execute if the condition is False

    
example :

"""
"""
a = 10

if a > 10 :
    print("A is greaterthan 10")
else:
    print("A is lessthan 10")

"""

"""
3. if-elif-else Statement

The if-elif-else statement allows testing multiple conditions sequentially. The first condition that evaluates to True is executed.

syntax :

if condition1:
    # Code to execute if condition1 is True
elif condition2:
    # Code to execute if condition2 is True
else:
    # Code to execute if none of the above conditions are True

"""    
# example :

"""
x = 10

if x > 10:
    print("x is greaterthan 10")
elif x < 10:
    print("x is lessthan 10")
else:
    print("x is equal to 10")

"""

"""
4. Nested if Statement

A nested if statement is an if statement inside another if or else block, allowing more complex decision-making.

syntax :

if condition1:
    if condition2:
        # Code to execute if both condition1 and condition2 are True
    else:
        # Code to execute if condition1 is True and condition2 is False
else:
    # Code to execute if condition1 is False

"""
# Example :

"""
x  = int(input("Enter a number : "))

if x > 10:

    if x % 2 == 0:
        print("x is greaterthan 10 and is even")
    else:
        print("x is greaterthan 10 and is odd")

elif x < 10:

    if x % 2 ==0:
        print("x is lessthan 10 and even ")
    else:
        print("x is lessthan 10 and odd")

else:
    print("x is equal to 10")

"""

# Real time examples :

# 1. Employee attendance Monitoring System :

"""
before 9.30 - ontime

before 10 - permission

after 10 - leave
"""

login_time = 12.40

if login_time <= 9.30:
    print("On-time")
elif login_time <=10:
    print("Permission")
else:
    print("Leave")