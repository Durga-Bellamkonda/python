#1.Constructing 2 lists containing all the available data types  (integer, float, string, complex and Boolean)
 
 
a = [17, 1.18, 'Bellamkonda', 8+28j, 'True', 18,17]
b = [17, 'False', 'Durga', 47.8, 5+4j,'Bellamkonda']

  #Creating another list by concatenating above 2 lists 
  
c = (a+b) 
print(c)  
#or
a.append(b)
print(a)
#or
a= [17, 1.18, 'Bellamkonda', 8+28j, 'True']
b = [25, 'False', 'Durga', 47.8, 5+4j]


a.extend(b)
print(a)

 #Find the frequency of each element in the concatenated list.
 
from collections import Counter
Counter(c)

 #or
print(c.count(17))
print(c.count(1.18))
print(c.count('Bellamkonda'))
print(c.count(8+28j))
print(c.count(True))
print(c.count(18))
print(c.count(False))
print(c.count('Durga'))
print(c.count(47.8))
print(c.count(5+4j))



 #Print the list in reverse order.
 
list=[125,'Naresh',450,'Mounika',65.78,3j,67]

list.reverse()
print(list)




#2.	Create 2 Sets containing integers (numbers from 1 to 10 in one set and 5 to 15 in other set)

set1={1,2,3,4,5,6,7,8,9,10}
set2={5,6,7,8,9,10,11,12,13,14,15}
print(set1.isdisjoint(set2))

	#Find the common elements in above 2 Sets.

lis = set1.intersection(set2)
lis

#or 
lis = set1&set2
lis



	#Find the elements that are not common.

lis = set1^set2
lis


# 	Remove element 7 from both the Sets
set1.remove(7)
set1


set2.remove(7)
set2

lis.remove(7)
lis


#or

n=7

if n in set1:
    set1.remove(n)

else:
    print('element does not exist in the set')
    
set1
    


if n in set2:
    set2.remove(n)

else:
    print('element dose not exist in the set')

set2


 #3. Create a data dictionary of 5 states having state name as key and number of covid-19 cases as values.
 
covid_cases={'Andhra pradesh':2037,'Telangana':3584,'Tamilnadu':2000,'karnataka':3500,'kerala':4000}

covid_cases

    #Print only state names from the dictionary.

print(list(covid_cases.keys()))


#or
covid_cases.keys()

   #Update another country and it’s covid-19 cases in the dictionary.

covid_cases.update({'singapore':20000})
                 
print(covid_cases)


#Operators
  #1.A.Write an equation which relates   399, 543 and 12345 

x=12345
y=543
z=299

equation=22*y+z

if equation == x:
    print('it is valid relation')
    
else:
    print('it is invalid relation')


#1.B.“When I divide 5 with 3, I got 1. But when I divide -5 with 3, I got -2”—How would you justify it.

a=5
b=3

a//b


c=-5
d=3
c//d


e=a%b
print(e)


#2.a=5,b=3,c=10.. What will be the output of the following
 # A. a/=b
  #B. c*=5  

a=5
b=3
c=10

a/=b
c*=5
print(int(a))
print(c)


      # 3.# A. How to check the presence of an alphabet ‘s’ in word “Data Science” .
      
word = "Data Science"
alphabet = 'S'

if alphabet in word:
    print(f"The alphabet '{alphabet}' is present in the word '{word}'.")
else:
    print(f"The alphabet '{alphabet}' is not present in the word '{word}'.")  
    
  #or
  
    word = 'Data science'

if 's' in word:

   print('True')

else:

   print('False')
    
    
          #  B. How can you obtain 64 by using numbers 4 and 3 .

#To obtain 64 using the numbers 4 and 3, we can use exponentiation, as follows:

a=4
b=3
c=a**b
print(c)    

#In this case, the number 4 is the base, and 3 is the exponent. Raising 4 to the power of 3 gives you 64.

#Variables
#1.	What will be the output of the following (can/cannot):
#a.	Age1=5
#b.	5age=55

#The code we provided raises some syntax errors, as variable names must adhere to specific rules. In most programming languages, including Python, variable names cannot start with a number. Let's examine each line separately:

Age1 = 5
#The code assigns the value 5 to the variable named Age1. This line should not produce any errors assuming it is written in a programming language that allows variable names to start with a capital letter, such as Python.

5age = 55
#This line raises a syntax error because the variable name 5age starts with a number, which is not allowed in most programming languages. Variable names should typically begin with a letter or an underscore.

#Therefore, the code in line b would not produce the desired output and would result in a syntax error in many programming languages.


#2.	What will be the output of following (can/cannot):
#a.	Age_1=100
#b.	age@1 = 100


#The code we provided raises some syntax errors due to invalid variable names. In most programming languages, including Python, variable names must follow specific rules. Let's examine each line separately:

Age_1 = 100
#The code assigns the value 100 to the variable named Age_1. This line should not produce any errors as the variable name adheres to the rules. Variable names can contain letters, numbers, and underscores, but they cannot start with a number.

age@1 = 100
#This line raises a syntax error because the variable name age@1 contains an invalid character, the at sign (@). In most programming languages, variable names can only contain letters, numbers, and underscores. Special characters like @ are not allowed in variable names.

#Therefore, line b would produce a syntax error in most programming languages due to the use of the invalid character '@' in the variable name.


#In Python, we can delete variables using the del statement. The del statement removes a variable from memory, freeing up the resources associated with it. Here's how you can delete variables in Python:


# Creating variables
a = 5
b = "Hello"
c = [1, 2, 3]

# Deleting variables
del a
del b, c

# Attempting to access deleted variables will raise an error
print(a)  # Raises NameError: name 'a' is not defined
print(b)  # Raises NameError: name 'b' is not defined
print(c)  # Raises NameError: name 'c' is not defined
#In the above example, the variables a, b, and c are created, and then the del statement is used to delete them. After deleting the variables, attempting to access them will result in a NameError because they no longer exist in memory.

#Note that deleting a variable is different from assigning it a value of None. Deleting a variable removes it completely, while assigning it a value of None means the variable still exists but doesn't currently have any meaningful value assigned to it.



















