def main() -> None:
    """
    Main function.
    """
    print('Starting the program...')
    while True:
        print('#### Menu ####')
        print('1. sum')
        print('2. subtract')
        print('3. multiply')
        print('4. divide')
        print('5. bigger_number')
        print('6. smaller_number')
        print('7. average')
        print('8. exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            # Perform addition
            x = int(input('Enter first number: '))
            y = int(input('Enter second number: '))
            result = x + y
            print(f'The sum of {x} and {y} is: {result}')
        elif choice == '2':
            # Perform subtraction
            x = int(input('Enter first number: '))
            y = int(input('Enter second number: '))
            result = x - y
            print(f'The difference between {x} and {y} is: {result}')
        elif choice == '3':
            # Perform multiplication
            x = int(input('Enter first number: '))
            y = int(input('Enter second number: '))
            result = x * y
            print(f'The product of {x} and {y} is: {result}')
        elif choice == '4':
            # Perform division
            x = int(input('Enter first number: '))
            y = int(input('Enter second number: '))
            if y != 0:
                result = x / y
                print(f'The division of {x} by {y} is: {result}')
            else:
                print('Error: Division by zero is not allowed.')
        elif choice == '5':
            # Find bigger number
            x = int(input('Enter first number: '))
            y = int(input('Enter second number: '))
            if x > y:
                print(f'The bigger number is: {x}')
            else:
                print(f'The bigger number is: {y}')
        elif choice == '6':
            # Find smaller number
            x = int(input('Enter first number: '))
            y = int(input('Enter second number: '))
            if x < y:
                print(f'The smaller number is: {x}')
            else:
                print(f'The smaller number is: {y}')
        elif choice == '7':
            # Calculate average
            x = int(input('Enter first number: '))
            y = int(input('Enter second number: '))
            result = (x + y) / 2
            print(f'The average of {x} and {y} is: {result}')
        elif choice == '8':
            print('Exiting the program...')
            break
        else:
            print('Invalid choice. Please try again.')
    print('Program ended.')
if __name__ == '__main__':
    main()