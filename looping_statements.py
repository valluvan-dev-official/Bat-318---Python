"""
Explanation of Loops in Python

    Loops in Python allow you to execute a block of code multiple times. Python supports two main types of loops: for loops and while loops.


1. For Loop

    A for loop is a control flow statement in programming that 
allows you to execute a block of code repeatedly for a 
specific number of times. It's particularly useful when
you know in advance how many times you want to execute a 
certain piece of code.


Key Features:

Used to iterate over a sequence like a list, tuple, dictionary, set, or string.
Executes a set of statements for each item in the sequence.
Iteration is finite and predefined by the length of the sequence.


syntax :

for variable in iterable:
    # Code to execute for each item

    
Example:

    Let's say you have a list of numbers and you want 
to print each number in the list. You can use a for loop
to iterate through the list and print each element

"""

fruits = ["apple","orange","lemon","Berry","mango","lichie","banana","Cherry"]

 
"""
for fruit in fruits: # ap or ma ba

    data = len(fruit) # 5 6 5 6

    if data > 5:
        print(fruit) # or ba

"""

# Breank and Continue :

"""
for fruit in fruits:

    # if 'a' not in fruit:

    if "Berry" in fruit:
    #   break
        continue

    print(fruit)

"""

# Else in For loop :

"""
numbers = [1,2,3,4,5]

for i in numbers:
    if i == 3:
        # break
        continue
    print(i) 
else:
    print("Loop completed")

"""

# Nested Loops :

students = ["Arun","Varun","Monisha"]

subjects = ["Tamil","English","Maths","Science"]

for std in students: # A  V  M
    
    print(f"{std} oda Subjects : ")

    for sub in subjects: # T E M S   T E M S   T E M S
 
        print(sub)

    print("-------------")