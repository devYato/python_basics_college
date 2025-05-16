def ask_user_for_number() -> int:
    """
    Ask the user for a number.
    """
    while True:
        try:
            user_input = int(input("Please enter a number: "))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def ask_user_for_operation() -> str:
    """
    Ask the user for a mathematical operation.
    """
    while True:
        operation = input("Please enter an operation (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            return operation
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")
            
def perform_operation(num1: int, num2: int, operation: str) -> float:
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        raise ValueError("Invalid operation")

def main():
    num1 = ask_user_for_number()
    operation = ask_user_for_operation()
    num2 = ask_user_for_number()
    result = perform_operation(num1, num2, operation)
    print(f"The result of {num1} {operation} {num2} is {result}")

if __name__ == "__main__":
    main()