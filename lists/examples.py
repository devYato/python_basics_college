# lists is a mutable sequence in Python
# lists are mutable sequences in Python
# lists can be changed after creation
# lists are defined using square brackets
# lists can contain any type of object
# lists can be nested
# lists can be empty
# lists can be created using the list() constructor
# ##### () --> tuples | [] --> lists | {} --> dictionaries
# ##### insert values examples #####
names = ['John', 'Jane', 'Jack', 'Jill']
names.insert(0, 'Jim')  # Insert 'Jim' at index 0
names.insert(2, 'Joe')  # Insert 'Joe' at index 2
names.insert(4, 'Judy')  # Insert 'Judy' at index 4
print(names)  # Output: ['Jim', 'John', 'Joe', 'Jane', 'Judy', 'Jack', 'Jill']

# ##### remove values examples #####
# Remove the first occurrence of 'Jack'
names.remove('Jack')
print(names)  # Output: ['Jim', 'John', 'Joe', 'Jane', 'Judy', 'Jill']
# Remove the first occurrence of 'Jill'
names.remove('Jill')
print(names)  # Output: ['Jim', 'John', 'Joe', 'Jane', 'Judy']

# Remove with pop 
# Remove the last element
last_name = names.pop()
print(last_name)  # Output: 'Judy'
print(names)  # Output: ['Jim', 'John', 'Joe', 'Jane']
# Remove the element at index 1
removed_name = names.pop(1)
print(removed_name)  # Output: 'John'
print(names)  # Output: ['Jim', 'Joe', 'Jane']

# We can also use the del statement to remove an element at a specific index
del names[1]  # Remove the element at index 1
print(names)  # Output: ['Jim', 'Jane']
# del names  # This will delete the entire list
# print(names)  # This will raise a NameError: name 'names' is not defined