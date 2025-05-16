# Task 3: Write a program that prints all numbers from 0 to 500 that are divisible by 3 and not even.

n = 0

for i in range(0, 501):
    if i % 3 == 0 and i % 2 != 0:
        print(f"{i} is divisible by 3 and not even")
        n += i
print(f"Sum of all numbers divisible by 3 and not even is {n}")