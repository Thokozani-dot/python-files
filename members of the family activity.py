
people = []


for i in range(10):

    name = input(f"Enter the name of person {i+1}: ")

    
    age = int(input(f"Enter the age of {name}: "))

    
    address = input(f"Enter the address of {name}: ")

    
    family_members = int(input(f"Enter the number of family members of {name}: "))

    password = f"{name}{age}{family_members}"

    
    people.append({
        "name": name,
        "age": age,
        "address": address,
        "family_members": family_members,
        "password": password
    })


for i, person in enumerate(people):
    
    if i > 14:
        print("The ID number exceeds 14. Exiting the program.")
        exit()

    
    print(f"Person {i+1}")
    print(f"Name: {person['name']}")
    print(f"Age: {person['age']}")
    print(f"Address: {person['address']}")
    print(f"Family Members: {person['family_members']}")
    print(f"Password: {person['password']}\n")
