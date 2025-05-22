one_to_20 = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten','eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')

x = int(input("Enter a number between 1 and 20: "))
if x < 1 or x > 20:
    print("Please enter a number between 1 and 20.")
else:
    print(f"The number you entered is: {one_to_20[x-1]}")