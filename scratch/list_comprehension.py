#!/usr/bin/python

#List comprehension syntax



fruits = ["apple", "orange", "grape", "watermelon", "cherry"]



'''

newlist = [expression for item in iterable if condition == True]

- newlist is the recipient list
- First x is item going into the recipient list
- Second x is refering to items in the extraction list
- The item from the extraction list gets pulled and added to destination list if the condition meets

'''

newlist = [x for x in range(10)]
print(newlist)

# here filtering is being done on the extraction side
newlist = [x for x in fruits if "a" in x]
print(newlist)

# here filtering is being done on the insertion side
newlist = [x if x != "grape" else "strawberry" for x in fruits]
print(newlist)

newlist = [x for x in fruits]
print(newlist)

#operation being done on the insertion side, word is being CAPATALIZED
newlist = [x.upper() for x in fruits]
print(newlist)
 
