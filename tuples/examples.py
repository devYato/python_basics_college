# Tuples are immutable sequences in Python
# They cannot be changed after creation
# Tuples are defined using parentheses
# Tuples can contain any type of object
# Tuples can be nested
# Tuples can be empty
# Tuples can be created using the tuple() constructor
##### () --> tuples | [] --> lists | {} --> dictionaries
##### Examples #####

# Creating a tuple

games = ('COD', 'WOW', 'BG3', 'POE', 'LAST EPOCH')
for game in games:
    print(game)
    print(f'This is the type of {game}: {type(game)}')
# Tuples are immutable so if you try to change a value in the tuple, it will raise an error
# games[0] = 'NEW GAME'  # This will raise a TypeError
    if type(game) == str:
        print(f"{game} is a string")
        game = game.lower().capitalize()
        print(f"After modification: {game}")
print(games)

print('=' * 40)
print(games[0])
print(games[1:4])
print(games[-1])
print(games[-2:])
print('=' * 40) 

# games[0] = 'NEW GAME'  # This will raise a TypeError

# we can use a for with enumerate to get the index and the value
for index, game in enumerate(games):
    print(f"Index: {index}, Game: {game}")