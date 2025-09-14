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


# 1. copy() : returns a copy of the list
# 2. list() : creates a list object


"""
cars = ["BMW","Audi","Tata","Maruti","Hyundai"]

# my_cars = cars.copy()

my_cars = list(cars)

print(my_cars)

"""

# ========= Join List Items ==========

# 1. + operator
# 2. extend()
# 3. append()

"""
a = [1,2,3]

b = [4,5,6]

c = a + b

print(c)

"""


# ============ Tuple ===============

"""
    is used to store multiple items in a single variable
    - Ordered
    - Unchangeable
    - Allows Duplicates
    - Indexed
    - can store different data types
    - we cannot change,add,remove items in a tuple after it has been created
    - we can use tuple() constructor to create a tuple

"""

# fruits = ('apple','banana','cherry','orange')

# print(fruits)
# print(type(fruits))


# fruits =('apple',)

# print(fruits)
# print(type(fruits))


# Constructor : tuple()

# x = tuple([234])

# print(x)
# print(type(x))


# ========= Access Tuple Items : =========

# fruits = ('apple','banana','cherry','orange',"mango","grapes")

# print(fruits[2])

# fruits[2] = "kiwi"  # we cannot change the value of a tuple

# print(fruits[0:5:2])


# =========== update tuple items ==========
"""
    we cannot change,add,remove items in a tuple after it has been created

    but we can convert the tuple into a list ,change the list and convert it back to tuple

"""

# fruits = ('apple','banana','cherry','orange',"mango","grapes")

# x = list(fruits)

# x[1] = "kiwi"

# fruits = tuple(x)

# print(fruits)


# ========= Unpack a tuple ==========

# Using asterisk * :

"""
fruits = ('apple','banana','cherry',"mango","grapes","orange")

*green,yellow,red = fruits

print(green)
print(yellow)
print(red)

"""

# ========= Join Tuple ==========

# 1. + operator
# 2. multiply operator *

"""
fruits = ('apple','banana','cherry')
vegetables = ('carrot','potato','brinjal')

# all_items = fruits + vegetables

all_items = fruits * 3

print(all_items)


"""


# ========= Set Methods ==========          


"""

    A set is a collection which is unordered, unchangeable*, and unindexed. 
    In Python sets are written with curly brackets.

    - Unordered
    - Unindexed
    - No Duplicates Allowed

    we can store different data types in a set

    we can add or remove items in a set after it has been created

    set do not allow duplicate values

    {}

    we can use set() constructor to create a set

    True and 1 are considered as a same value in a set and are treated as duplicates

    False and 0 are considered as a same value in a set and are treated as duplicates

"""

# Examples :

"""
my_set = {10,"Hello",True,1345.5,10,0,False,("apple","banana","cherry","orange")}

fruits = ["apple","banana","cherry","orange"]


print(my_set)

"""

# Constructor : set()


"""
myset = set(("apple","banana","cherry","orange","apple","Hello",100,234))


print(myset)    
print(type(myset))

"""

# Access Set Items :

"""
    we cannot access items in a set by referring to an index or a key
    but we can loop through the set items using a for loop , or we can use in keyword to check if an item exists in the set

"""

# fruits = {"apple","banana","cherry","orange"}

# for item in fruits:

#     print(item)


# ======== Add Set Items : ========

# 1. add() : add a single item to the set
# 2. update() : add multiple items to the set (can be list,tuple,set)

# add() :

"""
fruits = {"apple","banana","cherry"}

fruits.add("orange")
fruits.add("kiwi")

print(fruits)

"""


# update() :


"""
cars = {"BMW","Audi","Tata"}

cars.update(("Maruti","Hyundai"))

print(cars)

# my_set = {10,"Hello",True,1345.5,10,0,False,("apple","banana","cherry","orange")}

# print(my_set)

"""

# Join Two Sets :

# 1. union() : returns a new set with all items from both sets
# 2. update() : inserts all items from one set into another


"""
a = {"apple","banana","cherry"}
b = {"orange","mango","kiwi"}

c = a.union(b)

print(c)

"""
# Remove Set Items :

# 1. remove() : removes the specified item, raises an error if the item does not exist
# 2. discard() : removes the specified item, does not raise an error if the
# 3. pop() : removes the last item, raises an error if the set is empty
# 4. clear() : removes all the items in the set
# 5. del : deletes the set completely



# Common and Uncommon Items :

# 1. intersection() : returns a set that contains the items that exist in both sets
# 2. intersection_update() : removes the items that are not present in both sets
# 3. symmetric_difference() : returns a set that contains all items from both sets, except the items that are present in both sets
# 4. symmetric_difference_update() : removes the items that are present in both sets
# 5. difference() : returns a set that contains the items that exist in the first set but not in the second set
# 6. difference_update() : removes the items that are present in both sets from the first set


# Example :

# set1 = {"apple","banana","cherry","orange"}

# set2 = {"google","microsoft","apple"}


# result = set1.intersection(set2)

# result = set2.difference(set1)

# print(result)


# print(set1)

# set1.intersection_update(set2)

# set2.difference_update(set1)

# print(set2)



# Symmetric Difference :

"""
    The symmetric_difference() method returns a set that contains all items from both sets, except the items that are present in both sets.

    The symmetric_difference_update() method removes the items that are present in both sets, leaving only items that are unique to each set.
"""

# result = set1.symmetric_difference(set2)

# print(result)

# set1.symmetric_difference_update(set2)

# print(set1)



# ========= Dictionary ==========

"""
mydict = {
    "name" : "John",
    "age" : 30,
    "city" : "New York"
}

    - Key : value pairs
    - Ordered
    - Changeable
    - No Duplicates Allowed

    - can store different data types
    - we can change,add,remove items in a dictionary after it has been created
    - we can use dict() constructor to create a dictionary

"""

# Examples :

"""
my_dict = {"name":"John","age":30,"city":"New York","work":"John"}

print(my_dict)
print(type(my_dict))

"""

# Constructor : dict()

"""
my_dict = dict(name = "John", age = 30 , city = "Chennai")

print(my_dict)
print(type(my_dict))

"""


# Access Dictionary Items :

"""
    we can access the items of a dictionary by referring to its key name

    we can also use the get() method to access the items

"""

# Employee = {"name":"Harish","age":24,"city":"Chennai","work":"Developer"}

# print(Employee.get("name"))

# print(Employee["city"])


#  ======== get values ========

# values() :

# print(Employee.values())


# keys() :

# print(Employee.keys())


# items() :

# print(Employee.items())


# ============== Change Dictionary Items : ==============

# Using keyname :

# Employee = {"name":"Harish","age":24,"city":"Chennai","work":"Developer"}

# Employee["work"] = "Manager"

# Update() :

# Employee.update({"city":"Bangalore"})

# print(Employee)


# ============== Add Dictionary Items : ==============

# Using keyname :

# Employee = {"name":"Harish","age":24,"city":"Chennai","work":"Developer"}

# Employee["email"] = "harish@example.com"

# Employee.update({"phone":1234567890})

# print(Employee)


# ============== Remove Dictionary Items : ==============

# 1. pop() : removes the item with the specified key name
# 2. popitem() : removes the last inserted item
# 3. del : removes the item with the specified key name
# 4. clear() : removes all the items in the dictionary


Employee = {"name":"Harish","age":24,"city":"Chennai","work":"Developer"}


# pop() :

# Employee.pop("age")


# popitem() :

# Employee.popitem()


# del :

# del Employee["city"]

# del Employee


# clear :

Employee.clear()

print(Employee)