#we can make list of lists
customers = [
    ['John', 'Doe', 30],
    ['Jane', 'Smith', 25],
    ['Jack', 'Johnson', 40]
]

# Print the list of customers
for customer in customers:
    print(customer)
    
# append a new customer
customers.append(['Jill', 'Brown', 35])
# Print the updated list of customers
for customer in customers:
    print(customer)
# remove a customer
customers.remove(['Jack', 'Johnson', 40])
# Print the updated list of customers
for customer in customers:
    print(customer)
