# %%

x = 20 # int
print(type(x))

#%%

x = 20.5 # float
print(type(x))

#%%

# Strings are denoted by either
# single-quote or double-quotes
x = '20'
print(type(x))

x = "20"
print(type(x))

#%%

# bool
x = True
print(type(x))

x = False
print(type(x))

#%%

# NoneType; equivalent to NULL
x = None
print(type(x))

#%%

# list - can contain any type
x = ['john', 36, 1.7]
print(type(x))

# retrieve
print(x[0])     # prints 'john'
print(x[1])     # prints 36
print(x[2])     # prints 1.7

# update
x[0] = 'mary'

# prints ['mary', 36, 1.7]
print(x)  

#%%

# a tuple: immutable, ordered
x = (1, 2, 3)
print(type(x))

# cannot modify a tuple!
#x[0] = 4    # does not work!

# iterate each tuple
for item in x:
    print(item)

# to define a tuple of 1 element
y = (4)
print(y)

#%%
# dict - name/value pairs
x = {
    'name': 'john',
    'age': 36,
    'height': 1.7
}
print(type(x))

# retrieve
print(x['name'])    # prints 'john'
print(x['age'])     # prints 36
print(x['height'])  # prints 1.7

# update
x['name'] = 'mary'

# prints {'name':'mary','age':36,'height':1.7}
print(x)

#%%

# None
x = None

# ensures that x is of the correct
# data type for increment later on
if x == None:
    x = 1

x += 1
print(x)

#%%

#if-else condition
a = 10

if a == 1:
    print("a = 1")
elif a <= 5:
    print("a <= 5")
else:
    print("a = {}".format(a))

#%%

#While loop
# init variable x with 1
x = 1

# stops after x reaches 4
while x < 5:
    print("x = {}".format(x))
    x += 1

#%%

# Loop control
# the code prints 1 2 3 4 5
x = 0
while True:
    # increment x by 1
    x += 1
    print(x)

    # skip to start of loop for
    # every values of 2
    if x % 2 == 0:
        continue

    # exit loop if x exceeds 3
    if x > 3:
        break

#%%

# For Loops
# x is a list
x = ["john", 36, 1.7]

# access by index
for i in range(len(x)):
    print(x[i])

# access by item
for item in x:
    print(item)

#%%

arr = [1, 2, 3]

'''
Find the first position of x in array.
Returns position if found; -1 otherwise.
'''
def exists(arr, x):
    for i, val in enumerate(arr):
        if val == x:
            # returning position
            return i
    # not found
    return -1

# make function-call
pos = exists(arr, 3)

if pos == -1:
    print("Not Found")
else:
    print("Pos: {}".format(pos));

# %%

#Slicing
# creating a list
x = [1, 2, 3, 4, 5]

# slicing x
print(x[0:5])   # prints [1,2,3,4,5]
print(x[1:3])   # prints [2,3]
print(x[2:5])   # prints [3,4,5]

# updating first 3 values
x[0:3] = [10, 9, 8]
print(x)        # prints [10, 9, 8, 4, 5]

# start-idx missing (defaults to 0)
print(x[:3])    # prints [10, 9, 8]

# end-idx missing (defaults to len(x))
print(x[3:])    # prints [4, 5]

#%%

# creating a string
s = 'hello'

# start-index not specified; 
# defaults to 0
print(s[:3])   # prints hel

# end-index not specified; 
# defaults to end of list
print(s[2:])   # prints llo

#%%

#Negative Indexing
# creating a list
x = [1, 2, 3, 4, 5]

# negative indexing
print(x[-1])     # prints 5
print(x[-2])     # prints 4

# slicing with negative-indexing
print(x[-3:-1])  # prints [3, 4]
print(x[-1:])    # prints [5]
print(x[:-1])    # prints [1, 2, 3, 4]

# updating with negative-indexing
x[-1] = 10
x[-2] = 9

print(x)    # prints [1, 2, 3, 9, 10]

#%%

class APrivateClass:
    # constructor
    def __init__(self):        
        self.__private_attr = "I'm private"

    def _should_not_be_invoked_outside_class(self):
        print("I'm a private method")

privcl = APrivateClass()
#print(privcl.__private_attr) #error issue
privcl._should_not_be_invoked_outside_class()

#Class inheritance
class Employee:
    def __init__(self, name, year_of_birth, company):        
        # updating two instance-variables
        self.name = name
        self.year_of_birth = year_of_birth
        self.company = company

    def self_intro(self):
        print("My name is {}, born in {} and work at {}.".format(
            self.name, self.year_of_birth, self.company)) 


emp = Employee("John", 1971, "NUS")
emp.self_intro()

# %%
class APrivateClass:
    # constructor
    def __init__(self):
        self._private_attr = "I'm private"
    def _should_not_be_invoked_outside_class(self):
        print("I'm a private method")
# %%
class Person:
    # constructor
    def __init__(self, name, year_of_birth):
        # updating two instance-variables
        self.name = name
        self.year_of_birth = year_of_birth
    def self_intro(self):
        print("My name is {} and I'm born in {}.".format(
            self.name, self.year_of_birth))
# creating a new person object
john = Person("John", 1971)
john.self_intro()
# %%
class Employee(Person):
    def __init__(self, name, year_of_birth, company):
        # updating two instance-variables
        self.name = name
        self.year_of_birth = year_of_birth
        self.company = company
    def self_intro(self):
        print("My name is {}, born in {} and work at {}.".format(
            self.name, self.year_of_birth, self.company))
emp = Employee("John", 1971, "NUS")
emp.self_intro()
# %%
