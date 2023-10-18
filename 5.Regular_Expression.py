
##################################### Regular Expression #####################################
#regular is used to clean the data using patterns
import re
x = re.search("rat", "A cat and a rat can't be friends.")
print(x)
#it gives index of the cat

x = re.search("cow", "A cat and a rat can't be friends.")
print(x)

# In the previous example we had to import the module re to be able to work with regular expressions. 
# Then we used the method search from the re module. This is most probably the most important 
# and the most often used method of this module. re.search(expr,s) checks a string s 
# for an occurrence of a substring which matches the regular expression expr. 


# Let's assume that we have not been interested in the previous example to recognize the word cat, 
# but all three letter words, which end with "at". 
# The syntax of regular expressions supplies a metacharacter ".", 
# which is used like a placeholder for "any character".
#Here dot is placeholder which means any character can come
r" .at "
x = re.search(r" .at ", "A cat and a rat can't be friends.")
print(x)
# This RE matches three letter words, isolated by blanks, which end in "at".
# Now we get words like "rat", "cat", "bat", "eat", "sat" and many others.

# But what if the text contains "words" like "@at" or "3at"?

# Square brackets, "[" and "]", are used to include a character class. 
# [xyz] means e.g. either an "x", an "y" or a "z".

r"M[ae][iy]er" 
# Maier,Mayer,Meier,Meyer
# This is a regular expression, which matches a surname with four different spellings: Maier, Mayer, Meier, Meyer.

# We might need e.g. a class of letters between "a" and "e" or between "0" and "5". 
# To manage such character classes, the syntax of regular expressions supplies a metacharacter "-". 
# [a-e] a simplified writing for [abcde] or [0-5] denotes [012345].
# [ABCDEFGHIJKLMNOPQRSTUVWXYZ] we can write [A-Z].
# "any lower case or uppercase letter" [A-Za-z]
# Another Metacharacter is "^" which can be used inside square brackets
# If it is used directly after an opening sqare bracket, it negates the choice.
# If it is not positioned as the first character following the opening square bracket, it has no special meaning. 
# Similarly "-" also if positioned at first means match with "-"

import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# The special sequences consist of "\\" and a character from the following list:
# \d  Matches any decimal digit; equivalent to the set [0-9].
# \D  is not of \d. It matches any non-digit character; equivalent to the set [^0-9].
# \s  Matches any whitespace character; equivalent to [ \t\n\r\f\v].
# \S  The complement of \s. It matches any non-whitespace character; equiv. to [^ \t\n\r\f\v].
# \w  Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]. With LOCALE, it will match the set [a-zA-Z0-9_] plus characters defined as letters for the current locale.
# \W  Matches the complement of \w.
# \b  Matches the empty string, but only at the start or end of a word.
# \B  Matches the empty string, but not at the start or end of a word.
# \\  Matches a literal backslash.


# Quantifiers
# A quantifier after a token, which can be a single character or 
# group in brackets, specifies how often that preceding element is 
# allowed to occur. The most common quantifiers are
# the question mark ?
# the asterisk or star character *, which is derived from the Kleene star
# and the plus sign +, derived from the Kleene cross
########################################################
# *	             #         Match zero or more times.   #
# +	             #         Match one or more times.    #
# ?	             #         Match zero or one time.     #
# { n }	         #         Match exactly n times.      #
# { n ,}	     #         Match at least n times.     #
# { n , m }	     #         Match from n to m times.    # 
########################################################
##########################################################################
# MetaCharacters #	Description                                          #
# \	             #  Used to drop the special meaning of character        #
#                #  following it                                         #
# []	         #  Represent a character class                          #
# ^	             #  Matches the beginning                                #
# $	             #  Matches the end                                      #
# .	             #  Matches any character except newline                 #
# |              #  Means OR (Matches with any of the characters         #
#                #  separated by it.                                     #
# ?              #  Matches zero or one occurrence                       #
# *              #  Any number of occurrences (including 0 occurrences)  #
# +              #  One or more occurrences                              #
# {}             #	Indicate the number of occurrences of a preceding    #
#                #  regex to match.                                      #
# ()             # 	Enclose a group of Regex                             #
##########################################################################

# We used the fact the re.search() returns a match object if it matches 
# and None otherwise. We haven't been interested e.g. 
# in what has been matched. The match object contains a 
# lot of data about what has been matched, positions and so on.

import re

Nameage = '''Sharat is 35 and Pavan is 28 and Kaleem is 25 and Ganesh is 16'''

# re.findall()
# Return all non-overlapping matches of pattern in string, 
# as a list of strings. The string is scanned left-to-right, 
# and matches are returned in the order found.

# Example: Finding all occurrences of a pattern 

age = re.findall(r'\d{1,2}', Nameage)
names = re.findall(r'[A-Z][a-z]*', Nameage)
print(age)
print(names)

agedict = {}

x = 0

for eachname in names:
     agedict[eachname] = age[x]
     x += 1
     
print(agedict)

txt = "The rain in Spain"
x = re.split("\s", txt) # space character
print(x)

import re

string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+' # means one or more digit [0-9]

result = re.split(pattern, string) 
print(result)

import re

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub('#.*$', "", phone)
print("Phone Num : ", num)

# Remove anything other than digits
num = re.sub('\D', "", phone)    
print("Phone Num : ", num)

import re

allname = re.findall("name", "My name is Sharat and what is your name")
print(allname)

for name in allname:
    print(name)

# Find match pattern
    
import re

names = "Aam, Bam, Sam, Ram, Mam, Jam, Fan"

allnames = re.findall("[A-M]am", names) 
print(allnames)

for i in allnames:
    
    print(i)

import re

#Replaces the first two occurrences of a white-space character with the digit 9:

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

## dividing num, alpha, special char
import re

re.sub("[A-Za-z]", "*", "ada 1231zxdq #@$@zxfsd312")

re.sub("[^A-Za-z]", "&", "ada 1231zxdq #@$@zxfsd312")

## Remove white space

randstr = ''' 
My 
name 
is 
Deepthi
'''
print(randstr)

# re.compile() 
# Regular expressions are compiled into pattern objects, 
# which have methods for various operations such as searching 
# for pattern matches or performing string substitutions. 

regex = re.compile("\n")

randstr = regex.sub("", randstr)

print(randstr)

################################ re.sub function ######################################
# Python regex sub() function that returns a string after replacing the matched pattern in a string with a replacement.

# Introduction to the Python regex sub function
# The sub() is a function in the built-in re module that handles regular expressions. The sub() function has the following syntax:

# re.sub(pattern, repl, string, count=0, flags=0)
# Code language: Python (python)
# In this syntax:

# pattern is a regular expression that you want to match. Besides a regular expression, the pattern can be Pattern object.
# repl is the replacement
# string is the input string
# count parameter specifies the maximum number of matches that the sub() function should replace. If you pass zero to the count parameter or completely skip it, the sub() function will replace all the matches.
# flags is one or more regex flags that modify the standard behavior of the pattern.
# The sub() function searches for the pattern in the string and replaces the matched strings with the replacement (repl).

# If the sub() function couldn’t find a match, it returns the original string. Otherwise, the sub() function returns the string after replacing the matches.

# Note that the sub() function replaces the leftmost non-overlapping occurrences of the pattern. And you’ll see it in detail in the following example.

# Python regex sub function examples
# Let’s take some examples of using the regex sub() function.

# 1) Using the regex sub() function to return the plain phone number
# The following example uses the sub() function to turn the phone number (212)-456-7890 into 2124567890 :

## Number

import re

randstr = "12345"

print(len(re.findall("\d", randstr)))

print(re.search("\d{1}", randstr))

## Pan number verification 

import re

#\d [0-9] - digits
#\w [a-zA-Z0-9_] - alphanumeric


pan = "4669-5495-AA1212hhwjjwkq3"

if re.search("\d{4}-\d{4}-\w{15}", pan):
    
    print("it is a Pan No.")
    
else:
    print("its not a Pan No.")


import re

name = "My name is Yashvi, you tell me what is your name"

re.split(" ", name)

import re

string = "Python programming is fun"

# check if 'Python' is at the beginning
match = re.search('\APython', string)

if match:
  print("pattern found inside the string")
else:
  print("pattern not found")  

# Output: pattern found inside the string

import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")
