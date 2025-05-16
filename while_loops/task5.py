# fibonacci with while loop
def fibonacci(n):
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

# Test the function
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"Fibonacci sequence up to {n}: {fibonacci(n)}")