# Variables
message = "Hello World, people!"
print(message)

message = "Well, new one!"
print(message)

# Naming Rules
# Can: Letters, Numbers, Underscores
message_25 = "25 is here."

# Can't: 
# - Start w numbers
# 2message
# - No spaces
# message 1
# - No keywords
# if, for, etc.

# Best Practices:
# - Short but descriptive
hello = 'Hello World!'
print(hello)

# NameError
# print(helo)

# Exercises
# 1- Print a description of yourself, stored in a variable with descriptive name.
# 2- Change the value of the variable to something else (anything) and print it.

# Strings
ch = 'a'
ch = "a"

desc = 'My name is Bedir. Im 25, I live in Canada!'
print(type(desc))

# Functions
name = 'beDir tApkAn'

print(name.title())
print(name.upper())
print(name.lower())

# String concatenation
# (+)
first_name = 'BeDir'
last_name = 'tapKan'

print(first_name + ' ' + last_name)

full_name = first_name + ' ' + last_name
print(full_name.title())

# Whitespace
print('Hello World!')
# \t - tab
print('Hello\tWorld!')
# \t - t is never shown!
print('  \tea')
# \n - new line
print('Hello\nWorld!')

# Stripping Whitespaces
name = '    Bedir  '
last_name = 'Tapkan'
full_name = name + last_name
print(name.lstrip() + last_name)
# left strip
print(name.rstrip() + last_name)
# strip
print(name.strip() + last_name)
print(name.rstrip().lstrip() + last_name)

print(full_name + '-')

# Exercises:
# 1:
# - Store your first name, in lowercase, in a variable.
# - Using that one variable, print your name in lowercase, Titlecase, and UPPERCASE.

# 2:
# - Store your first name and last name in separate variables, 
#   and then combine them to print out your full name.

# 3:
# - Choose a person you look up to. Store their first and last names in separate variables.
# - Use concatenation to make a sentence about this person, and store that sentence in a variable.
# - Print the sentence.

# 4:
# - Store your first name in a variable, but include at least two kinds 
#   of whitespace on each side of your name.
# - Print your name as it is stored.
# - Print your name with whitespace stripped from the left side, then 
#   from the right side, then from both sides.

# Numbers
# Integer
print(3 + 2)
print(3 - 2)
print(5 * 2)
print(4 / 2)

# power
print(5 ** 2)

calc = 5 + 2 * 2
print(calc)

calc = (5 + 2) * 2
print(calc)

# Floating-point numbers
print(0.1 + 0.1)
print(0.1 + 0.2)

# Exercises:
# 1: 
# - Write a program that prints out the results of at least one calculation 
#   for each of the basic operations: addition, subtraction, multiplication, 
#   division, and exponents.

# 2: 
# - Find a calculation whose result depends on the order of operations.
# - Print the result of this calculation using the standard order of operations.
# - Use parentheses to force a nonstandard order of operations. Print the result 
#   of this calculation.

# 3:
# - On paper, 0.1+0.2=0.3. But you have seen that in Python, 0.1+0.2=0.30000000000000004.
#   Find at least one other calculation that results in a long decimal like this.

# COMMENTS
# is a comment this line operator
'''
This
is
a
multiline 
comment
'''
# import this

# - Write a program that uses everything you have learned in this notebook at least once.
# - Write comments that label each section of your program.
# - For each thing your program does, write at least one line of output that explains 
#   what your program did.