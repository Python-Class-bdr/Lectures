# Q1
# Topic: List Comprehensions
# Write out the following code without using a list comprehension:
# plus_thirteen = [number + 13 for number in range(1,11)]

# Q2
# Topic: List Comprehensions
# Using a list comprehension, create a list of the even indexed
# characters of every word in the strings below:
# "The quick brown fox jumps over the lazy dog."
# "My name is Inigo Montoya. You killed my father. Prepare to die."
# "Luke, I am your father"

# Q3
# Topic: String Manipulation
# Write a program that finds all the words that starts with the letter
# 'd' in the following strings:
# "A day without sunshine is like, you know, not a day."
# "Dreams come true. Without a dream, nothing happens."
# "Dry day in a drought."
# "Dance or die. The choice is dreadfully simple."

# Q4
# Topic: String Manipulation
# Change all the cat's to dog's in the following strings:
# "My cat is my best friend."
# "This cat is outrageous."
# "We have a cat problem."

# Q5
# Topic: String Manipulation
# Store a sentence in a variable. Using slices, print out
# the first five characters, any five consecutive characters
# from the middle of the sentence, and the last five characters
# of the sentence.

# Q6
# Topic: String Manipulation
# A string is simply an ordered collection of symbols selected
# from some alphabet and formed into a word; the length of a string
# is the number of symbols that it contains.

# An example of a length 21 DNA string (whose alphabet contains the
# symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

# Given: A DNA string s of length at most 1000 nt.

# Return: Four integers (separated by spaces) counting the respective
# number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

# Source: https://rosalind.info/problems/dna/

# Q7
# Topic: String Manipulation
# An RNA string is a string formed from the alphabet containing 'A', 
# 'C', 'G', and 'U'.

# Given a DNA string t corresponding to a coding strand, its transcribed
# RNA string u is formed by replacing all occurrences of 'T' in t with 'U'
# in u.

# Given: A DNA string t having length at most 1000 nt.

# Return: The transcribed RNA string of t.

# source: https://rosalind.info/problems/rna/

# Q8
# Topic: String Manipulation
# In DNA strings, symbols 'A' and 'T' are complements of each other,
# as are 'C' and 'G'.

# The reverse complement of a DNA string s is the string sc formed by
# reversing the symbols of s, then taking the complement of each symbol
# (e.g., the reverse complement of "GTCA" is "TGAC").

# Given: A DNA string s of length at most 1000 bp.

# Return: The reverse complement sc of s.

# source: https://rosalind.info/problems/revc/

# Q9
# Topic: General
# - Make a list of the most important words you have 
#   learned in programming so far. You should have terms such as list,
# - Make a corresponding list of definitions. Fill your list with 'definition'.
# - Use a for loop to print out each word and its corresponding definition.
# - Maintain this program until you get to the section on Python's Dictionaries.

# Q10
# Topic: Functions
# - Many songs follow a familiar variation of the pattern of verse, 
#   refrain, verse, refrain. The verses are the parts of the song 
#   that tell a story - they are not repeated in the song. The refrain
#   is the part of the song that is repeated throughout the song.
# - Find the lyrics to a song you like that follows this pattern. 
#   Write a program that prints out the lyrics to this song, 
#   using as few lines of Python code as possible.


# BONUS QUESTIONS
# ---------------
# Q1
# Topic: List Comprehensions
# Write a program that prints out the first 10 powers of 2.

# Q2
# Topic: Functions
# Write a program that takes in a string and prints out the number of
# times that the string "bob" appears in the given string.

# Q3
# Topic: Functions
# Write a program that takes in a string and prints out whether or not
# the string is a palindrome. A palindrome is a word or phrase that is
# the same forwards and backwards.

# Q4
# Topic: Functions
# Write a program that takes in a string and prints out the number of
# vowels in the string.

# Q5
# Topic: String Manipulation, Functions
# Write a function that converts a strings letters alternating between
# upper and lower case.

# Q6
# Read the Python styling guides summary here; 
#
# Indentation
# - Use 4 spaces for indentation. This is enough space to give
#   your code some visual structure, while leaving room for 
#   multiple indentation levels. There are configuration settings 
#   in most editors to automatically convert tabs to 4 spaces, and 
#   it is a good idea to check this setting. On Geany, this is under 
#   Edit>Preferences>Editor>Indentation; set Width to 4, and Type to 
#   Spaces.

# Line Length
# - Use up to 79 characters per line of code, and 72 characters for comments. 
#   This is a style guideline that some people adhere to and others completely 
#   ignore. This used to relate to a limit on the display size of most monitors. 
#   Now almost every monitor is capable of showing much more than 80 characters 
#   per line. But we often work in terminals, which are not always high-resolution. 
#   We also like to have multiple code files open, next to each other. It turns 
#   out this is still a useful guideline to follow in most cases. There is a 
#   secondary guideline of sticking to 99 characters per line, if you want longer 
#   lines.
# - Many editors have a setting that shows a vertical line that helps you keep 
#   your lines to a certain length. In Geany, you can find this setting under 
#   Edit>Preferences>Editor>Display. Make sure "Long Line Marker" is enabled, 
#   and set "Column" to 79.

# Blank Lines
# - Use single blank lines to break up your code into meaningful blocks. You 
#   have seen this in many examples so far. You can use two blank lines in longer 
#   programs, but don't get excessive with blank lines.

# Comments
# - Use a single space after the pound sign at the beginning of a line. If you 
#   are writing more than one paragraph, use an empty line with a pound sign 
#   between paragraphs.

# Naming Variables
# - Name variables and program files using only lowercase letters, underscores, 
#   and numbers. Python won't complain or throw errors if you use capitalization, 
#   but you will mislead other programmers if you use capital letters in variables 
#   at this point.

# source: https://www.python.org/dev/peps/pep-0008/
