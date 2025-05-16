user_input = str(input('Please enter a phrase: '))
# Check if the input is empty
if not user_input:
    print("You entered an empty string.")
else:
    reversed_input = user_input[::-1]
    print(f"Reversed phrase is: {reversed_input}")
    if user_input.replace(" ", "").lower() == reversed_input.replace(" ", "").lower():
        print(f"The phrase {user_input} is a palindrome.")