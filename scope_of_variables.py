# Scope OF Variables :

"""

    Defines the Accessbility of variables.
    A variable scope specifies the region where we can access a variable.

    There are three types of Scope :

        1. Local Scope 
        2. Global Scope
        3. Non Local Scope

"""


# local scope :

"""
a variable that is defined inside a function has local scope.
it can be accessed only inside the function.
it is not accessible outside the function.
Defined inside a function and accessible only within it.

"""

# Example :

"""
def myfun():

    name = "Kamal"

    print(name)


myfun()

print(name)

"""


# Non Local Scope :


"""
def Outer_function():

    name = "Varun" # Non Local

    def inner_function():

        print(name)

    inner_function()

    

Outer_function()

"""
