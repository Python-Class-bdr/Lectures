# While Loops
# while condition:
#     run the code as long as condition is satisfied
health = 5

while health > 0:
    print(f"Still fighting..! Health: {health}")

    health = health - 1
print("You are dead now.")

# Exercise
# 0: (5 points - each)
# Make a variable called strength, and set its initial value to 5.
# Print a message reporting the player's strength.
# Set up a while loop that runs until the player's strength increases to a value such as 10.
# Inside the while loop, print a message that reports the player's current strength.
# Inside the while loop, write a statement that increases the player's strength.
# Outside the while loop, print a message reporting that the player has grown too strong, and that they have moved up to a new level of the game.
# Bonus: Play around with different cutoff levels for the value of strength, and play around with different ways to increase the strength value within the while loop.
strength = 5
print(f"Strength: {strength}")
while strength < 10:
    print(f"Strength: {strength}")
    strength = strength + 1
print("You have grown too strong!")
print("You have moved up to a new level of the game.")


# INPUT TAKING
# variable = input('Message')
# it takes a str
names = ["bedir"]
another_name = input("A name I should know: ")
names.append(another_name)

print(names)

# Exercise 1:
# 0:
# Make a list that includes 3 or 4 games that you like to play.
# Print a statement that tells the user what games you like.
# Ask the user to tell you a game they like, and store the game in a variable such as new_game.
# Add the user's game to your list.
# Print a new statement that lists all of the games that we like to play (we means you and your user).
games = ["csgo", "dota 2", "league (awful)", "sims4"]
for game in games:
    print(game)
new_game = input("A game you like: ")
games.append(new_game)
for game in games:
    print(game)

# While loops - keep it running
new_name = ""
names = []
while new_name != "quit":
    new_name = input("Give me a name (type quit if you want to stop): ")
    if new_name != "quit":
        names.append(new_name)
print(names)

# Dictionaries
l = [3, 4]
l[0]

# dct = {}
# dct = {
#     key: value
# }
dct = {"bedroom": "beautiful room", 3: "hi there"}
print(dct["bedroom"])
print(dct[3])

for key, value in dct.items():
    print(key, ":", value)

#####
# dictionary_name = {
#     key1: value1,
#     key2: value2,
#     ...
# }

attributes = {"bedir": "is tall", "tarik": "has dark hair", "huze": "wears glasses"}

name = "bedir"
print(f"{name} {attributes[name]}")

for key, value in attributes.items():
    print(f"{key} {value}")

# Exercise:
# 0:
# Create a dictionary to hold information about pets. Each key is an animal's name, and each value is the kind of animal.
# For example, 'ziggy': 'canary'
# Put at least 3 key-value pairs in your dictionary.
# Use a for loop to print out a series of statements such as "Willie is a dog."
animals = {"hannah": "dog", "boncuk": "cat", "foggy": "goat"}
for key, value in animals.items():
    print(f"{key.title()} is a {value}.")
