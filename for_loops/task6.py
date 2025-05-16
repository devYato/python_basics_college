user_term_input = int(input('Please enter a term number: '))
user_constant_input = int(input('Please enter a constant number: '))

if user_constant_input == 0:
    print("Constant cannot be zero.")
elif user_constant_input < 0:
    for i in range(user_term_input, 0, user_constant_input):
        print(i)
elif user_constant_input > 0:
    for i in range(0, user_term_input+1, user_constant_input):
        print(i)