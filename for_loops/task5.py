n = 0
for i in range(0, 6+1):
    if i % 2 == 0:
        print(f"{i} is even")
        n += i
print(f"Sum of all even numbers from 0 to 6 is {n}")