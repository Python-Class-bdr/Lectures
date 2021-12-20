# Lists and Tuples

# Lists
students = ['tarik', 'diana', 'yusuf', 'nilgun', 'jonas', 'huze']

# Naming and Defining
# variable_name = [items]
colors = ['r', 'g', 'b']

# Accessing elements
# 0, 1, 2, 3, ..., n
# ith element -> name_of_the_var[i]
the_color = colors[0]
print(the_color)
print(colors[1])

# access reverse
print(colors[-1])

# no no no
# print(colors[-4])
# IndexError: list index out of range
# print(colors[3])

# Exercises 0
# 0:
# - Store the values 'python', 'c', and 'java' in a list. 
#   Print each of these values out, using their position in the list.

# 1:
# - Store the values 'python', 'c', and 'java' in a list.
#   Print a statement about each of these values, using their position in the list.
#   Your statement could simply be, 'A nice programming language is value.'

# 2:
# - Think of something you can store in a list. Make a list with three or four items, 
#   and then print a message that includes at least one item from your list. 
#   Your sentence could be as simple as, "One item in my list is a __."


# Loops in Lists
names = ['bedir', 'tarik', 'ayca', 'allie', 'nil']

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

for name in names:
    print(name)

# syntax
# for var_name in list_name:
# -> whatever code to run

for x in names:
    print(x + ' is not that great.')
    print('And ' + x + ' knows it!')
print("That's all a joke!")

# Enumerate
tech_comps = ['microsoft', 'apple', 'google']

for i, comp in enumerate(tech_comps):
    print(str(i + 1) + '-' + comp.title())
    # print((i + 1) + ' ' + comp.title())
    print((i + 1), comp.title())

l1 = ['1', '2', '3', '4']
l2 = ['one', 'two', 'three']
for i in range(len(l2)):
    print(l1[i], l2[i])

l2[3]

# Exercises
# 0:
# - Repeat Exercise 0-0, but this time use a loop to print out each value in the list.

# 1:
# - Repeat Exercise 0-1, but this time use a loop to print out your statements.
#   Make sure you are writing the same sentence for all values in your list. 
#   Loops are not effective when you are trying to generate different output for 
#   each value in your list.

# 2:
# - Repeat Exercise 0-2, but this time use a loop to print out your message for 
#   each item in your list. Again, if you came up with different messages for each 
#   value in your list, decide on one message to repeat for each value in your list.

# Common Op.
# Modify
tech_comps = ['microsoft', 'apple', 'google']
tech_comps[0] = 'amazon'

print(tech_comps)

# Find
print(tech_comps.index('apple'))
# print(tech_comps.index('microsoft'))
# ValueError: 'microsoft' is not in list

# If exists
print('microsoft' in tech_comps)
print('apple' in tech_comps)

# Appending
tech_comps.append('microsoft')
print(tech_comps)

# Inserting
tech_comps.insert(2, 'deepMind')
print(tech_comps)

social_medias = []

# add comps
social_medias.append('facebook')
social_medias.append('instagram')
social_medias.append('whatsapp')

for i, sm in enumerate(social_medias):
    print(str(i + 1) + '-' + sm.title())

# sorting a list
tech_comps.sort()
for i, tc in enumerate(tech_comps):
    print(str(i + 1) + '-' + tc.title())

# Reverse sort
tech_comps.sort(reverse=True)
for tc in tech_comps:
    print(tc)

# sort vs sorted
tech_comps_sorted = sorted(tech_comps)
print(tech_comps)
print(tech_comps_sorted)

# Exercise
# 0: Reverse print a list
rev = ['a', '1', '2', 'me']
print(rev[::-1])
rev.reverse()
print(rev)

# Numerical sorting
nums = [1, 3, 2, 5, 4]
print(sorted(nums))
print(sorted(nums, reverse=True))
nums.reverse()
print(nums)

# lenght
length = len(nums)
print(length)

# Exercises 3:
# 0:
# - Start with the list you created in Exercise 0:0.
# - You are going to print out the list in a number of different orders.
# - Each time you print the list, use a for loop rather than printing the raw list.
# - Print a message each time telling us what order we should see the list in.
    # - Print the list in its original order.
    # - Print the list in alphabetical order.
    # - Print the list in its original order.
    # - Print the list in reverse alphabetical order.
    # - Print the list in its original order.
    # - Print the list in the reverse order from what it started.
    # - Print the list in its original order
    # - Permanently sort the list in alphabetical order, and then print it out.
    # - Permanently sort the list in reverse alphabetical order, and then print it out.

# 1:
# - Make a list of 5 numbers, in a random order.
# - You are going to print out the list in a number of different orders.
# - Each time you print the list, use a for loop rather than printing the raw list.
# - Print a message each time telling us what order we should see the list in.
    # Print the numbers in the original order.
    # Print the numbers in increasing order.
    # Print the numbers in the original order.
    # Print the numbers in decreasing order.
    # Print the numbers in their original order.
    # Print the numbers in the reverse order from how they started.
    # Print the numbers in the original order.
    # Permanently sort the numbers in increasing order, and then print them out.
    # Permanently sort the numbers in descreasing order, and then print them out.

# 2:
# - Copy two or three of the lists you made from the previous exercises, or make up two or three new lists.
# - Print out a series of statements that tell us how long each list is.

# remove 
# by pos
nums = [1, 3, 2, 5, 4]
del nums[0]
print(nums)

# by val
nums.remove(2)
print(nums)

nums = [2, 2, 3, 4]
nums.remove(2)
print(nums)

# pop
nums = [1, 2, 3, 4, 5]
last = nums.pop()
print(nums)
print(last)

one = nums.pop(0)
print(nums)
print(one)

# Exercise:
# 0:
    # Make a list that includes the names of four famous people.
    # Remove each person from the list, one at a time, using each of the four methods we have just seen:
        # Pop the last item from the list, and pop any item except the last item.
        # Remove one item by its position, and one item by its value.
    # Print out a message that there are no famous people left in your list, and print your list to prove that it is empty.

# slicing
# var_name[start_idx:stop_index:step_size]
# [0:end:1]
nums = [1, 2, 3, 4, 5]
print(nums[0:3])
print(nums[::2])

copy_nums = nums[:]
copy_nums_wrong = nums
nums[0] = 4
print(nums)
print(copy_nums)
print(copy_nums_wrong)

# range
# range(start, end, step)
for n in range(1, 11, 2):
    print(n)

nums = list(range(1, 11, 2))
print(nums)

# min, max, sum
ages = [23, 25, 35, 18, 16, 77]

youngest = min(ages)
oldest = max(ages)
total_age = sum(ages)

print(youngest, oldest, total_age)