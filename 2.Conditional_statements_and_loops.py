# Conditional Statements / Control Flow

# Example: - if condition 

a = 23

if a >= 22:
   print("if")


x = 3


if x < 5:
    print(x)
print(5)

x = 2
y = 25
print(x)

if x < 10:
    print(x)
print(y)


# Example: - if and else conditions when you have two conditions

is_male = False

if is_male:
    print("you are male")
else:
    print("you are female")

a = 23

if a >= 22:
   print("if")
   print("one more statement")
elif a >= 21:
   print("elif")
else:
   print("else")


# Example: - if you have more than two conditions use elif 

is_male = True
is_tall = True 

if is_male and is_tall:              ## and & not operator 
    print("you are tall male")
elif is_male and not(is_tall):
    print("you are short male")
elif not(is_male) and is_tall:
    print("you are not male and tall")
else:
    print("you are not male and not tall")


#Example: - conditional inside a conditional 
### Nested if Statement

score = 500
money = 6000
age = 65

if score > 100:
    print("You got good points")    
    if money >= 5000:
        print("You win")         
        if age >= 30:
            print("You win in middle age")
        else:
            print("You win in young age")
    else:
        print("You have high points but you do not have enough money")       
else:
    print("You are loser")


# Testing for an element in list
list = ['Ajay', 'Ramesh']
if 'Vijay' in list:
    print('Found Vijay')




# **Loops in Python**

# **Why Loops ?**

# We use loops because if we need to repeat some set of instructions multiple
# times then instead of writing multiple lines fo code we can use loops to 
# perform those operation in a few line and with easy process. 
# Let's go through an example - if you have to print "hello world" 1000 times 
# then we need to write print statement 1000 time but using loops you can 
# easily do it in a few lines.


# **Loops :** Loops in programming language means repeating a set of 
# instructions until a specific condition is fulfilled.

# **Types of loops in Python ?**


# 1. For Loop: Repeats the set of instructions until condition is false. 
#              It checks condition before excuting the body part of loop 
# 2. While Loop: Executes set of instructions and the code that manage the loop
# 3. Nested loop: Here you can use loop inside the 'for' loops or 'while' loops


# **How to control loops or control statements in Python ?**

# * Continue statement: Continue specific part of loop till the condition 
#                       is true and leave remaining part of the loop
# * Break statement: Break the loop and get out of loop when condition is met
# * Pass Statement: When we don't want to run the condition or do not want 
#                   to print anything then we use pass statement


# # For loop
# To use 'for' loop we use **for** keyword with a variable or range, or pre-defined data types (i.e., set, tuple, list, dict, string). This loop ends with a colon.

# Next line always starts with indentation (four space).

# If we don't use indentation then we can get out of the loop


# Example for 'for loop' 

# Example:
    
snacks = ['pizza', 'burger', 'shawarma', 'franky']

for snack in snacks:
    print("current snack: ", snack)   
print("Good day!")


range(0, 5) # range function but it will not return values

a = list(range(0, 15))   # TypeError: 'list' object is not callable

range(1, 5, 1)

for i in range(1, 6, 2):
    print(i)
else:
    print("The for loop is over")

for i in range(1, 15):
  print("20 hours class of Day ", i)


# Getting even number without any condition

for i in range(0, 15, 2):
  print('Number is even', i)


# Traversing a list

numbers = [2, 3, 5]
sum = 0
for num in numbers:
    sum += num  #sum = sum+num
print(sum)

numbers = [2, 3, 5]
getsum = [i + 2 for i in numbers]
print(getsum)

numbers = [2, 3, 5]
getnum = [i + 2 for i in numbers if i < 5]
print(getnum)

# Example:
num = int(input("number: "))
factorial = 1 

if num < 0:
    print("must be positive")
elif num == 0:
    print("factorial = 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("factorial =  ", factorial)



## Pass

names = ["Rishu", 'Aayush', 'Ram', 'Shubh']

for i in names:
    pass



## Continue

names = ["Rishu", 'Aayush', 'Ram', 'Shubh']

for i in names:
  if len(i) == 3:
    continue
  print(f'My name is {i}')



## Break

names = ["Rishu", 'Aayush', 'Ram', 'Shubh']

for i in names:
  if len(i) == 3:
    break
  print(f'My name is {i}')

for i in range(1, 10):
       if i == 5:
           break
       print(i)
print('Done')


## For - else
# If the 'else' statement is used with a 'for' loop, the 'else' block is 
# executed only if 'for' loops terminates normally (and not by encountering 
# break statement)

# Example
numbers = [11, 33, 55, 39, 55, 75, 37, 21, 23, 41, 13]

for num in numbers:
   if num % 2 == 0:
      print ('the list contains an even number')
      break
else:
  print ('the list does not contain even number')


names = ["Rishu", 'Aayush', 'Ram', 'Shubh']
list(enumerate(names))


names = ["Rishu", 'Aayush', 'Shubh', 'Ram']

for i, j in enumerate(names):
  print('index is {0} and value of index is {1}'.format(i, j))



# While Loop
# To apply 'while' loop we use keyword **while** with the condition and end
# line with a colon.

# We also need to specify an iteration based on a condition which will make
# the 'while' loop stop otherwise 'while' loop will continue exeucting. 

i = 0
while i < 10:
  print('Number is ', i)
  i = i + 1
  

i = 0
while i < 10:
  pass
  i = i + 1


i = 0
while i < 10:
  i = i + 1
  if i == 5:
    continue
  print('Number is ',i)


i = 0
while i < 10:
  i = i + 1
  if i == 5:
    break
  print('Number is ', i)


i = 0
while i < 10:
  print('Number is ', i)
  i = i + 1
else:
  print('Loop has ended')



# Nested Loops

# Here we can use loop inside a loop multiple times. 

list1 = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(list1, '\n')

for i in list1 :
    for j in i :
        print(f'Square of {j} is', j ** 2)
    print("\n")

# Best Example for nested loop

# Print triangle shaped star

n = 6  # number of star
k = n + 1   # spaces
for i in range(0, n) :
    for j in range(0, k) :
        print(" ", end = "")
    k = k - 1                  # Reducing spaces after each loop
    for j in range (0, i + 1) :      # Taking new loop for printing *
        print("* ", end = "")
    print("\r")  # After completion of printing '*', start again from new line
 