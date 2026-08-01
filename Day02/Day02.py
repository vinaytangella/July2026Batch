# Data Types
i = 10 #int
s = 'rohit' #strings
r = 10.0 #float
c = 2 + 3j #complex
b = True #boolean
n = None #none

print(type(c))

sum = 10 + 23 + 67.2

print('------------------------')
print('before ',id(s))
s = s + ' kumar' #concatenating 
print('------------------------')
print('after 1', id(s))
print('------------------------')
s = s + ' is a software engineer'
print('------------------------')
print('after 2', id(s))
print('------------------------')
#instr = str(i) + s # type casting

# stri = int(s) + i



# immutable and mutable data types
# string is immutable
# run out of memory - python handles this?
# memory management in python - garbage collector  - 
# heap and stack (memory areas)
# stack is fastest - heap is slow
# stack - noodles, masala, bowl, water (easy to access place - fast) local varibales
# heap - class objects

class Car:
    pass

cobj = Car()

cobj - basic data type

int - python already has knowledge - int = 10 
j = 10

"""
https://docs.python.org/3.12/reference/lexical_analysis.html#keywords
git repo - git set up - git clone, checkouts,
"""
