user_input = int(input('Type a number and i will give you the factorial: '))
factorial = 1
while user_input > 0:
    factorial *= user_input
    user_input -= 1
print(f'The factorial is: {factorial}')