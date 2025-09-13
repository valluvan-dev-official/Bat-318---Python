# List :

"""
    is used to stroe multiple items in a single variable

    - Ordered
    - Changeable
    - Allows Duplicates
    - Indexed

    we can store different data types in a list

    we can change,add,remove items in a list after it has been created

    []


"""


# fruits = ['apple','banana','cherry','orange']

# print(fruits)

# print(type(fruits))


# List constructor : list()


"""
data = list((234,456,678))

print(data)

print(type(data))

"""

# Access List Items :

"""
    - use index number to access list items
    - positive or negative indexing

"""

"""
fruits = ['apple','banana','cherry','orange',"mango","grapes"]


# print(fruits[0])

# print(fruits[-4])

# print(fruits[-4:-2])

# print(fruits[0:5:2])

print(fruits[-5::2])

"""

# check an item in list :

# fruits = ['apple','banana','cherry','orange',"mango","grapes"]

# print('banana' in fruits)



# ========= Change List Items ==========


"""
fruits = ['apple','banana','cherry','orange',"mango","grapes"]

# fruits[2] = "Mango"

fruits[1:4] = ["kiwi"]

print(fruits)

"""

# ========= Add List Items ==========

# 1. append() : add item to the end of the list
# 2. insert() : add item at the specified index
# 3. extend() : add elements of a list (or any iterable), to the end of the current list


# fruits =["apple","banana","cherry"]

# Append  

"""
fruits.append("Orange")

fruits.append("kiwi")

"""

# Insert :

"""
fruits.insert(1,"Mangossss")

fruits.insert(-1,"Mango")

"""

# extend () :

"""
vegetables = ["carrot","potato","brinjal"]

# fruits.append(vegetables)

fruits.extend(vegetables)

"""
# print(fruits)



# ========= Remove List Items ==========


# 1. remove() : removes the specified item
# 2. pop() : removes the specified index, if index is not specified removes the last item
# 3. del : removes the specified index
# 4. clear() : removes all the items in the list


# fruits =["apple","banana","cherry","orange","kiwi","Mango"]

# Remove :

# data = fruits.remove("banana")

# POP :

# data = fruits.pop(2)

# data = fruits.pop()

# del :

# del fruits[2:5]

# del fruits

# clear :

# fruits.clear()

# print(data)

# print(fruits)



# ========= Sort List Items ==========


# 1. sort() : sort the list ascending or descending order

"""
    
    will sort the list alhabetically or numerically , ascending by default

    sort() casesensitive resulting capital letters are sorted before lower case letters

"""

# num = [34,12,45,67,89,23,1,9,0]


# num.sort() - > Ascending order

# num.sort(reverse=True) - > Descending order

# print(num)


# fruits =["apple","Grapes","banana","lemon","cherry","orange","Kiwi","Mango","Apple"]

# # fruits.sort()

# fruits.sort(reverse=True)

# print(fruits)


# ========= Copy List Items ==========