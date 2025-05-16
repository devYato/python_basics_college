gender = str(input('What is your gender? ')).lower()
# Check if the input is valid
while gender not in ['male', 'female']:
    print("Invalid gender. Please enter 'male' or 'female'.")
    gender = str(input('What is your gender? '))

age = int(input('What is your age? '))
while age < 0 or age > 120:
    print("Invalid age. Please enter a valid age between 0 and 120.")
    age = int(input('What is your age? '))