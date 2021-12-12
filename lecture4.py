# IF - ELSE
# Condition checher
# if condition:
#     code to run if true
# elif another condition:
#     code to run if another condition is true
# else:
#     code to run if none were true

# condition > true / false
desserts = ['ice cream', 'chocolate', 'apple crisp', 'baklava', 'cookies', 'katmer']
favorite_dessert = 'katmer'

for dessert in desserts:
    if dessert == favorite_dessert:
        print(f'{dessert} is my favorite!!')
    else:
        print(f'{dessert} is not the best...')

# Logical Tests
# a == b -> if a is equal to b (value)
# a != b -> if a is not equal to b (value)
# a > b
# a >= b
# a < b
# a <= b
# a in ls 
print(5 == 5)
print(6 == 5)
print(6 != 5)
print(3 > 3)
print(3 >= 3)

print(3 in [4, 5])
print('a' in 'car')

print('Cat' == 'cat')
print('Cat'.lower() == 'cat')

# Exercise
# 0:
#   - Write a program that consists of at least ten lines, each of which has a logical statement on it. The output of your program should be 5 Trues and 5 Falses.

students = ['bedir', 'tarik', 'yusuf', 'jonas', 'diana', 'huzeyfe', 'joseph']
if len(students) > 4:
    print('The class is big enough')

for student in students:
    if len(student) > 5:
        print(f'The letters here are too crowded: {student}')
    elif student[0] == 'j':
        print(f'Well, who do we have here! Such an honor: {student}')
    elif student[0] == 't':
        print(f'.. Why are you even here...: {student}')
    else:
        print(f'Well this one is just perfect: {student}')

# Exercise
# 0:
def crowd_test(people):
    if len(people) > 3:
        print('The room is too crowded.')
# Make a list of names that includes at least four people.
people = ['bedir', 'nilgun', 'tarik', 'jonas']
# Write an if test that prints a message about the room being crowded, if there are more than three people in your list.
crowd_test(people)
# Modify your list so that there are only two people in it. Use one of the methods for removing people from the list, don't just redefine the list.
people.pop()
people.pop()
# Run your if test again. There should be no output this time, because there are less than three people in the list.
crowd_test(people)
# Bonus: Store your if test in a function called something like crowd_test.


# 1:
    # Add an else statement to your if tests (from exercise 0). If the else statement is run, have it print a message that the room is not very crowded.

# 2:
    # Add some names to your list (from exercise 1), so that there are at least six people in the list.
    # Modify your tests so that
    # If there are more than 5 people, a message is printed about there being a mob in the room.
    # If there are 3-5 people, a message is printed about the room being crowded.
    # If there are 1 or 2 people, a message is printed about the room not being crowded.
    # If there are no people in the room, a message is printed about the room being empty.


# Every value has a truth value
def truth_value(value):
    if value:
        print(f'{value}, {type(value)} evaluates to True.')
    else:
        print(f'{value}, {type(value)} evaluates to False.')

# int
# 0 - false
# anything else is true
truth_value(0)
truth_value(1)
truth_value(-1)

# Strings
truth_value(' ') # tarik
truth_value('_') # nilgun
truth_value('=') # diana
truth_value('\n') # yusuf
truth_value('^') # jonas
truth_value('{}') # huzeyfe
truth_value('')

# Special - None
truth_value(None)

# Boolean / True - False
truth_value(True)
truth_value(False)

# Floats truth values?
truth_value(0.1)
truth_value(0.0)

# GROUPS SCORES
# N-T: 10
# D-J: 10
# Y-H: 10

# Q1:
# 10 points
    # Make a list of ten aliens, each of which is one color: 'red', 'green', or 'blue'.
    # You can shorten this to 'r', 'g', and 'b' if you want, but if you choose this option you have to include a comment explaining what r, g, and b stand for.
    # Red aliens are worth 5 points, green aliens are worth 10 points, and blue aliens are worth 20 points.
    # Use a for loop to determine the number of points a player would earn for destroying all of the aliens in your list.    

# Q2:
# 20 points

# There are three groups of people in a class. The first group is the teachers, the second group is the students, and the third group is the parents.
# The teacher is worth 5 points, the students are worth 10 points, and the parents are worth 15 points.
# Use a for loop to determine the total number of points the class would earn if all groups were to give all of their points.
# If a student is missing their parents, they should not be counted.
# Make sure to include a comment explaining what the variables are.
# Make the program dynamic so that it can be run with any list of people. (use functions)
people = ['t', 't', 'p1', 'p2', 'p4', 'p6', 's1', 's2', 's2', 's5', 's4', 's3']
# t - p(int < 10) - s(int < 10)

def calculate_points(people):
    sum_points = 0
    for person in people:
        if person == 't':
            sum_points += 5
        elif person[0] == 'p':
            sum_points += 15
        else:
            num = person[1]
            if 'p' + num in people:
                sum_points += 10
    print(sum_points)

calculate_points(people)



# Input sample:
# - [t, t, p1, p2, p4, p6, s1, s2, s5, s4, s3]
# Output:
# - 100


