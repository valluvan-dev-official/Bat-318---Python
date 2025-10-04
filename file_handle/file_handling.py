# file handling :
"""
r - read :
    default value.open a file for reading,error if does not exists.

a - append :
    open a file for appending, creates the file if it does not exists.

w - write :
    open a file for writing,creates the file if it does not exists

x - create :
    creates the specified file,returns an error if the file exists.

- In addition if the file should be handled as binary or text file.

    1. "t" - text - Default values text mode
    2. "b" - binary - Binary mode(ex: images)


open() :

    key function for working with files in python

    - open() function returns a file object

    takes two parameters: filename and mode 

    ex :
        file = open("filename","r")



read():
    - method for reading the content of the file.
    - By default the read() method returns the whole text,but you can
        also specify how many characters you want to return.

        
readline:

    - return oneline


# readlines() :

 - returns a list

 - containing each line in the file as a list item



"""


# r - mode :


# f = open("intro.txt","r")

# print(f.read(10))

# print(f.read())


# print(f.readline())
# print(f.readline())
# print(f.readline())

# print(f.readlines())



# w and a - mode :

# writing an existing file :

"""
"a" - will append to the end of the file

"w" - will overwrite any existing content.
    - will overwrite the entire file.
"""


# 1. append :


"""
f = open("intro.txt",'a')

f.write("\nI'm working in Chennai")

f.close()

"""

# f= open("intro_new.txt","w")

# f.write("Welcome to Chennai")

# f.close()

# 2. write : 

"""
f = open("intro.txt","w")

f.write("i'm a software developer")

f.close()

"""


# x - mode :

# f = open("intro_new.txt",'x')


# Delete a file :

# python - delete a file :
"""
to delete a file, you must import os module

"""

# import os 


# os.remove("intro_new.txt")

# check the file is exist or not :


"""
if os.path.exists("sample.txt"):

    print("file is Exists")

    os.remove("sample.txt")

else:

    print("The file is not Exist")

"""


# delete a folder :

"""
- you can remove only empty folder

"""

# os.rmdir("empty")


# Find a Mode in File Handling :

"""
f = open("intro.txt")

print(f.mode)

"""


# Readable() :

"""
 - used to check whether the specified file is readable or not.
 - it will take no parameter

"""

# Example :

"""
f = open("intro.txt")

print(f.readable())

f.close()

print(f.readable())

"""


# tell() :

"""
- returns current position of the file.
- it will take no parameters and returns an integer value.

"""

# Example :

"""
f = open("intro.txt")

print(f.tell())

print(f.read(20))

print(f.tell())

f.close()

"""

# seek() :

"""
- used to change the position of the file handle to a given position.
- file handle is like a cursor
- which position do you want to work 

"""

# Example :

"""
f = open("intro.txt")

print(f.seek(15))

print(f.read(10))

"""

# with statement in file handling :
"""
 - it simplifies the management of common resources like file streams.

 syntax :

  with openfile as variable:

"""


with open("intro.txt") as f:

    print(f.read())







