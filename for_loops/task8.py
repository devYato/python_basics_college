group = [
    {
        'name': 'Renann',
        'age': 25,
        'gender': 'male'
    },
    {
        'name': 'Ana',
        'age': 19,
        'gender': 'female'
    },
    {
        'name': 'Maria',
        'age': 18,
        'gender': 'female'
    },
    {
        'name': 'Lucas',
        'age': 22,
        'gender': 'male'
    }
]

def add_user_to_group() -> None:
    """
    Add user to the group.
    """
    how_many_users = int(input('How many users do you want to add? '))
    for _ in range(how_many_users):
        user = {
            'name': input('What is your name? '),
            'age': int(input('What is your age? ')),
            'gender': input('What is your gender? ')
        }
        group.append(user)
        print(f"User {user['name']} added to the group.")
        print('#' * 20)
        
def show_group() -> None:
    """
    Show the group.
    """
    if not group:
        print("The group is empty.")
    else:
        for user in group:
            print(f"Name: {user['name']}, Age: {user['age']}, Gender: {user['gender']}")
            
def check_group_age_mean() -> float:
    if not group:
        print('The group is empty.')
        return 0
    age_sum = sum(user['age'] for user in group)
    return age_sum / len(group)

def woman_under_20() -> None:
    """
    Show all women under 20 years old.
    """
    women = [user for user in group if str(user['gender']).lower() == 'female' and user['age'] < 20]
    if not women:
        print("No women under 20 found.")
    else:
        for user in women:
            print(f"Name: {user['name']}, Age: {user['age']}, Gender: {user['gender']}")

def main() -> None:
    while True:
        print("\nMenu:")
        print("1. Add user to group")
        print("2. Show group")
        print("3. Check group age mean")
        print("4. Show women under 20")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_user_to_group()
        elif choice == "2":
            show_group()
        elif choice == "3":
            mean_age = check_group_age_mean()
            if mean_age:
                print(f"The mean age of the group is: {mean_age}")
        elif choice == "4":
            woman_under_20()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()