import numpy as np

hello = "Hey there!"
for i in range(50):
    print(hello)

start = np.random.randint(1, 1000)
end = np.random.randint(1000, 3000)
for i in range(start, end):
    print(i)
print("The loop has ended.")

print('#' * 20)

for i in range(end, start, -1):
    print(i)
print("The loop has ended.")

print('#' * 20)