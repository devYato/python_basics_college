# Dictionary of examples for the `dicts` module
# dicts is a mutable mapping in Python
# dicts are mutable mappings in Python
# dicts can be changed after creation
# dicts are defined using curly braces
# dicts can contain any type of object
# dicts can be nested
# dicts can be empty
# dicts can be created using the dict() constructor
# ##### () --> tuples | [] --> lists | {} --> dictionaries
# ##### Examples #####
# Creating a dictionary
customers = {
    'John': {'last_name': 'Doe', 'age': 30},
    'Jane': {'last_name': 'Smith', 'age': 25},
    'Jack': {'last_name': 'Johnson', 'age': 40}
}
# Print the dictionary
for customer, details in customers.items():
    print(f"Customer: {customer}, Details: {details}") 
    
# Adding a new customer
customers['Jill'] = {'last_name': 'Brown', 'age': 35}
# Print the updated dictionary
for customer, details in customers.items():
    print(f"Customer: {customer}, Details: {details}")

# print(customers['Jill'])
print(customers.keys())
print(customers.values())
print(customers.items())