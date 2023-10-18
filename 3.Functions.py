# Functions

# Define function

# Example for advantages of functions 
    
# Imagine there are 100 lines of code created based on requirement without using functions.

print("Hello Function.Python") 
print("Hello Function.Python") 
print("Hello Function.Python") 
print("Hello Function.Python") 


def sayHello():
    print('Hello World!') # Block belonging to the function
# End of function #

sayHello()

# Not defined any value but defined an empty function 
def hello_func():              
    pass
hello_func()


# Simple function 
def hello(name, age, sal):                 
    print("hi", name, "your age:", age, "your salary:", sal)

hello("Sharat", 25, 50000)


# Formal and actual arguments

# Function definition
def add(a, b):
    return a + b


# function call
add(2, 3)


# Formal arguments are identifiers used in the function definition to represent corresponding actual arguments.
# Actual arguments are values (or variables / expressions) that are used inside the parentheses of a function call.


# Positional arguments
def rectangleArea(width, height):
    return width * height

print(rectangleArea(width = 1, height = 2))

# A positional argument is a name that is not followed by an equal sign (=) and default value.

def printMax(a, b):
   if a > b:
       print(a, 'is maximum')
   elif a == b:
       print(a, 'is equal to', b)
   else:
       print(b, 'is maximum')

printMax(3, 4) 


def say(message, times = 1):
   print(message * times)

say('Hello')
say('World ', 5)



        
def is_greater(a=10, b=20):
  if a>b:
    return 'yes'
  else:
    return 'No'
is_greater()        
        
    

def func(a, b = 5, c = 10):
   print('a is', a, 'and b is', b, 'and c is', c)
func(3, 7)
func(25, c = 24)
func(c = 50, a = 100)


x = 50
def func(x):
   print('x is', x)
   x = 2
   print('Changed local x to', x)
print('x is still', x)


x = 50
def func(x):
   print('x is', x)
   x = 2
   print('Changed local x to', x)
func(x)
print('x is still', x)


# Variable arguments
# *args for variable number of arguments 
def myFun(*argv):  
    for arg in argv:  
        print(arg) 
    
myFun('Hello', 'Welcome', 'to', '360digitmg')  


# Use **kwargs to pass the variable keyword arguments to the function 

def intro(**data):
    print("\nData type of argument:", type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))

intro(Firstname = "Sita", Lastname = "Sharma", Age = 22, Phone = 1234567890)
intro(Firstname = "John", Lastname = "Wood", Email = "johnwood@nomail.com", Country = "Wakanda", Age = 25, Phone = 9876543210)


def total(initial, *numbers, **keywords):
   count = initial
   for number in numbers:
       count += number
   for key in keywords:
       count += keywords[key]
   return count
print(total(10, 1, 2, 3, vegetables = 50, fruits = 100))


## Function call stack
### locals(), globals()

x = 5  #global 
def new():
  print('number is', x)

new()
print(x)

x = 5
def new():
  x = 10  #local
  print('number is', x)

new()
print(x)


age = 23 # Age Global variable
name = "Somesh" # Name Global Variable
places = ["Nagpur", "Mumbai", "Pune"] # Places Global Variable


def local(): # Function declaration  
    age = 1 # Age Local Variable
    name = 'Aayush' # Name Local Variable
    print("%s is %i years old and lives in %s." % (name, age, places[0])) # Function Definition for Local Variable
    # In the above line of code name and age variables are Local and place is Global Variable 
    return

local() # Function calls Local() Variables
print("##############")

print("%s is %i years old and lives in %s." % (name, age, places[2])) # Calling efinition for Global Variable
#In the above line of code name, age and place are Global Variables 


## Declaring global variable within function

x = 5
def new():
  global x
  x = 10   # global
  print('number is', x)

new()
print(x)


## Recursion

# A defined function can call itself.

def fact(N):
  if N < 0:
    print("Input the positive number")
  elif N == 0:
    print(f'Factorial of {N}! is {1}')
  else:
    fact = 1
    for i in range(1, N + 1):
      fact *= i
    print(f'Factorial of {N}! is {fact}')
    
fact(5)


def fact(N):
  if N < 0:
    print("Input the positive number")
  elif N == 0:
    print(f'Factorial of {N}! is {1}')
  elif N == 1:
    return 1
  else:
    return (N * fact(N-1))
    
fact(5)



# List Comprehensions

# List Comprehensions and Readability 

# Build a list of Unicode codepoints from a string in ordinary way 
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
     codes.append(ord(symbol))
codes 

# finding only odd numbers
list=[]
for i in range(50):
  if i % 2 ==1:
    list.append(i)
list
    

# Alternative way to perform the above Unicode using list comprehension
symbols = '$¢£¥€'
codes = [ord(symbol) for symbol in symbols] 
codes 


new_list = [i for i in range(12) if i % 2 == 1]
print(new_list)


## Dictionary Comprehension

# Let us see how the same problem can be solved using a for loop and dictionary comprehension
# We want to create a new dictionary where the key is a number divisible by 2 in a range of 0-10 and it's value is the square of the number.
numbers = range(10)
print(numbers)
new_dict_for = {}

# Add values to 'new_dict' using 'for' loop
for n in numbers:
    if n % 2 == 0:
        new_dict_for[n] = n ** 2

print(new_dict_for)

# Use dictionary comprehension
new_dict_comp = {n: n**2 for n in numbers if n % 2 == 0}

print(new_dict_comp)


##Another example
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

dict1_keys = {k * 2 : v * 2 for (k, v) in dict1.items()}
print(dict1_keys)



## Zip and Unzip

# Python code to demonstrate the working of zip()
# Initializing lists 
name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"] 
roll_no = [4, 1, 3, 2] 
marks = [40, 50, 60, 70] 
  
# Using zip() to map values 
mapped = zip(name, roll_no, marks) 
print(mapped)
  

# Converting values to print as set 
mapped = set(mapped) 
  
# Printing resultant values  
print("The zipped result is : ") 
print(mapped) 


# Unzipping values 
namz, roll_noz, marksz = zip(*mapped) 
  
print("The unzipped result: \n") 
print("The name list is : ", end = "") 
print(namz) 
print("The roll_no list is : ", end = "") 
print(roll_noz)   
print("The marks list is : ", end = "") 
print(marksz)



# Built-in Functions

### Sort

animals = ['cat', 'dog', 'sheep', 'goat', 'elephant']
# Ascending order with alphabet 
sorted(animals)


# Descending order with alphabet 
sorted(animals, reverse = True)


# Descending order with respect to length of the character
sorted(animals, key = len, reverse = True)


# Ascending order with respect to length of the character 
sorted(animals, key = len)


# Built-in function for sort
abcd = animals.sort()
print(abcd)


# Augmented Assignments with Sequences

# Explanation of mutability and immutability for list and tuple using memory location identity

# Augumented assignment operators with *=
# id of lists 
l = [1, 2, 3]
print(id(l), l)
# ID of list will not change, it will just append the values to the same ID
l *= 2 # Eql to l*2
print(id(l), l)


# Augumented assignment operators with *=
t = (1, 2, 3)
print(id(t), t)
# ID of the tuple will change instead of appending the values to the same ID 
t *= 2
print(id(t), t) 



# Handling Missing Keys

# Initializing Dictionariey
d = { 'a' : 1, 'b' : 2 }
# trying to output value of absent key
print("The Value associated with 'c' is :")
print(d['c'])

# we need to handle these kind of errors
# importing "collection" for defoault dict
import collections as cl

# Declaring defaultdict
# sets default value 'key Not found' to absent keys
defd = cl.defaultdict(lambda : 'key Not available')
# initializing values
defd['a'] = 1


# initializing values
defd['b'] = 2


# Printing value
print("The value of 'a' is : ", end = "")
print(defd['a'])


# Printing value associated with 'c'
print("The value of 'c' is : ", end = "")
print(defd['c'])



# Lambda Functions

# Defining the lambda function 
s = lambda x: x * x
s(12)


## map()
# map(function,  iterable)

val = [1, 2, 3, 4, 5, 6]

list(map(lambda x: x * 2, val))

list(map(str, val))

## filter() 
# filter (function returns true false,  iterable)

val1 = [1, 2, 3, 4, 5, 6]

list(filter(lambda x: x % 2, val1))     

print(list(filter(lambda x: x > 50, list(range(1, 100)))))


## reduce()
from functools import reduce

val = [1, 2, 3, 4, 5, 6]

reduce(lambda x, y: x * y, val)     # 1 * 2 * 3 * 4 * 5 * 6

reduce(lambda x , y: x + y, list(range(1, 100)))   # 1 + 2 + 3 + 4 + 5 ........

help(reduce)



## Loop vs Comprehension vs Map (lambda function)

list1 = [1, 2, 3, 4, 5]
squares1 = []

# Loop
for i in list1:
    squares1.append(i ** 2)
    
# Comprehension
squares2 = [i ** 2 for i in list1]

# map
squares3 = list(map(lambda x : x ** 2, list1))

squares1, squares2, squares3



## Iterators
# Iterator is an object which allows a programmer to traverse through all the 
# elements of a collection, regardless of its specific implementation.

names = ["Rishu", 'Aayush', 'Shubh', 'Ram']
print(names)   # iterable

new_list = names.__iter__()   # Converting into iterator
print(new_list)

help(new_list)

for obj in new_list:
  print(obj)

names = ["Rishu", 'Aayush', 'Shubh', 'Ram']
names   # iterable
print(next(names))

print(next(new_list))

new_list = iter(names)    # Another way of converting into iterator
print(next(new_list))

print(next(new_list))
print(next(new_list))
print(next(new_list))

for obj in names:
  print(obj)


# Why use iterator ?

# An **iterable** is an object that has an __iter__ method which returns an iterator, or defines a __getitem__ method that can take sequential indexes starting from zero. So an iterable is an object that you can get an iterator.

# An **iterator** is an object with a next (Python 2) or __next__ (Python 3) method.

# Whenever you use a 'for' loop, or map, or a list comprehension, etc., in Python, the next method is called automatically to get each item from the iterator, thus going through the process of iteration.

names = [i for i in range(1000000)]
new_list = iter(names)

import sys
print(f'size of variable names is {sys.getsizeof(names)} bytes')
print(f'size of variable new_list is {sys.getsizeof(new_list)} bytes')

iterable_value = 'Machine Learning'
iterable_obj = iter(iterable_value) 
  
while True: 
    try:   
        # Iterate by calling next 
        item = next(iterable_obj) 
        print(item) 
    except StopIteration:   
        # exception will happen when iteration stops
        break


## Generator
# A generator is a function that produces or yields a sequence of values using 'yield' method.

# When a generator function is called, it returns a generator object without even beginning execution of the function. When the next( ) method is called for the first time, the function starts executing until it reaches the yield statement, which returns the yielded value. The yield keeps track i.e., remembers the last execution and the second next( ) call continues from previous value.

# Simple function 
def squence(N):
  x = []
  for i in range(N):
    x.append(i)
  return x

alist = squence(10000)

print(alist)

def squence(N):  
  for i in range(N):
    yield i

blist = squence(100000)
print(blist)
print(next(blist))

print(f'size of variable new_list is', sys.getsizeof(alist), 'bytes')
print(f'size of variable new_list is', sys.getsizeof(blist), 'bytes')

# A simple generator for Fibonacci Numbers 
def fib(limit): 
      
    # Initialize first two Fibonacci Numbers  
    a, b = 0, 1
  
    # One by one yield next Fibonacci Number 
    while a < limit: 
        yield a 
        a, b = b, a + b 


# Create a generator object 
x = fib(5) 
print(x)


# Iterating over the generator object using next 
while True:
   try:
      print (next(x), end = "\n")
   except StopIteration:
      break


# String slicing ##
String ='DATA SCIENTIST'
  
## Using indexing sequence ##
print(String[:6])
print(String[1:5:3])
print(String[-1:-14:-3])
