# List Comprehensions
squares = []

# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
for number in range(1, 11):
    new_square = number ** 2
    squares.append(new_square)

for square in squares:
    print(square)

# ** - num1 ** num2 
squares = [number ** 2 for number in range(1, 11)]

print(squares)

nums = [(number + 2) * 3 for number in range(1, 11)]

# Non-numerical versions
students = ['jonas', 'yusuf', 'diana']

great_students = []
for student in students:
    great_students.append(student.title() + ' the great...')

for great_student in great_students:
    print('Hello ' + great_student)

# great_students = [add 'the great' to each student, for each student in the list of students]
great_students = [student.title() + ' the great!' for student in students]
for great_student in great_students:
    print('Hello ' + great_student)

squares = [number ** 2 for number in range(1, 11)]
# EXERCISES 1:
# 0:
    # Make a list of the first ten multiples of ten (10, 20, 30... 90, 100). 
    # There are a number of ways to do this, but try to do it using a list comprehension. 
    # Print out your list.
# 1:
    # We saw how to make a list of the first ten squares. Make a list of the first ten cubes 
    # (1, 8, 27... 1000) using a list comprehension, and print them out.
cubes = [num ** 3 for num in range(1, 11)]
# 2:
    # Store five names in a list. Make a second list that adds the phrase "is awesome!" to each name, 
    # using a list comprehension. Print out the awesome version of the names.
# 3:
    # Write out the following code without using a list comprehension:

    # plus_thirteen = [number + 13 for number in range(1,11)]

# Strings as Lists
s = 'Bedir'
for letter in s: # iterable
    print(letter)

ls = list(s)
print(ls)

# num = 2000
# for n in num:
#     print(n)

# Slicing strings
name = 'Braddock'
first_ch = name[0]
last_ch = name[-1]

first_4_letters = name[:4]
last_4_letters = name[-4:]

print(first_4_letters)
print(last_4_letters)

sentence = 'He was the champ!'
print(sentence[3:6])

word = 'peanut butter'
print(word[5::-1])

# Finding substrings
message = 'He fought for all!'
all_present = 'all' in message
print(all_present)

all_index = message.find('all')
print(all_index)
print(message[all_index:all_index+len('all')])

msg = 'Cats and dogs... Cats and dogs...'
print(msg.find('Cats'))
print(msg.rfind('Cats'))

# replace
print(msg.replace('dogs', 'turtles'))

# count
print(msg.count('dogs'))

# Splits
sentence = 'The hockey team lost'
ls = sentence.split(' ')
print(ls)

weird_sent = 'Here-we-are-why-here'
ls = weird_sent.split('-')
print(ls)
ls = weird_sent.split('W')
print(ls)

animals = 'cat, dog, turtle, hamster, lion'
print(animals.split(', '))

# Tuples
# immutable - never can change
colors = ('red' , 'green', 'blue')
print(colors[0])

for color in colors:
    print(color)

# colors[0] = 'Red'
# colors.append('purple')
# colors.pop()

# String formatting with numbers
# print('Hi ' + 23)
num = 23
print('Hi ' + str(num))

print('Hi there beautiful number %d.' % num)

ls = [7, 13, 19]
print('Some of the amazing prime numbers are %d, %d, and %d.' % (ls[0], ls[1], ls[2])) 
print('Some tries: %s %d %f' % ('hey there', 3, 3.0))

# %s - string
# %d - int
# %f - floats

print('A float: %.2f' % 3.0)
float_number = 3.0
print(f'A float: {float_number}, {num}')

print('Some of the amazing prime numbers are {}, {}, and {}.'.format(ls[0], ls[2], ls[1]))

# Variable types
# String

# Int
a = 2

# Float
f = 3.0

# Bool
# True and False
val = True
val = False

# Basic math operators
a = 3 + 2 # sum
a = 3 - 2 # sub
a = 4 * 2 # mult
a = 5 / 2 # div
a = 5 // 2 # div - wo remainder
a = 5 % 2 # remainder
a = 5 ** 2 # power

# FUNCTIONS
# def function_name(arguments):
    # whatever the action we need

# function_name(arguments)
print('You are an amazing person Allie!')
print('We are appriciating your existence...')
print('Please spend more time with us.')
print('To enroll, click the button below!')

print('You are an amazing person Tarik!')
print('We are appriciating your existence...')
print('Please spend more time with us.')
print('To enroll, click the button below!')

print('You are an amazing person Jonas!')
print('We are appriciating your existence...')
print('Please spend more time with us.')
print('To enroll, click the button below!')

print('You are an amazing person Nilgun!')
print('We are appriciating your existence...')
print('Please spend more time with us.')
print('To enroll, click the button below!')

# ad_run('Nilgun')

def ad_run(name):
    print(f'You are an amazing person {name}!')
    print('We are appriciating your existence...')
    print('Please spend more time with us.')
    print('To enroll, click the button below!')

ad_run('Nilgun')
ad_run('Jonas')
ad_run('Diana')
ad_run('Huzeyfe')

def email_students(message, emails):
    for email in emails:
        print(f'Sent to: {email}')
        print(f'Message: {message}')

emails = ['em1@gmail.com', 'e2@gmail.com', 'f3@gmail.com', 'gg5@gmail.com']

message = 'Students must bring a pen!'
email_students(message, emails)

message = 'Also an eraser please...'
email_students(message, emails)

message = 'No pen, meant pencil!'
email_students(message, emails[:2])

def get_number_of_words(sentence):
    ls = sentence.split(' ')
    return len(ls)

message = 'The world is an amazing place!'
lenght = get_number_of_words(message)
print(lenght)

# EXERCISES
# 0:
    # Write a function that takes in a person's name, and prints out a greeting.
        # The greeting must be at least three lines, and the person's name must be in each line.
    # Use your function to greet at least three different people.
    # Bonus: Store your three people in a list, and call your function from a for loop.
# 1:
    # Write a function that takes in a first name and a last name, and prints out a nicely formatted full name, in a sentence. Your sentence could be as simple as, "Hello, full_name."
    # Call your function three times, with a different name each time.
# 2:
    # Write a function that takes in two numbers, and adds them together. Make your function print out a sentence showing the two numbers, and the result.
    # Call your function with three different sets of numbers.
# a = 3
# print(f'Hey {a}')

# name = input('What is your name: ')
# print(f'Hi {name}')

n1 = int(input('Number 1 to sum: '))
n2 = int(input('Number 2 to sum: '))
print(f'The sum is = {n1 + n2}')