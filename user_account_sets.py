# Simple program to manage two user accounts using sets

print("\nOptions:")
print("1. Add user to set_a")
print("2. Add user to set_b")
print("3. Print both sets")
print("4. Show combination of both sets (without duplicates)")
print("5. Show common values between both sets")
print("6. Show difference (values only in set_a)")
print("7. Exit")

while True:
    choice = int(input("Enter a choice:"))   # user input for menu choice

    # Add a user to set_a
    if choice == 1:
        name = input("Name of the user: ")
        contact = input("Enter the contact of the user: ")
        city = input("Enter the city of the user: ")
        account = input("Enter the account no: ")
        a = {name, contact, city, account}   # storing user info in set_a

    # Add a user to set_b
    elif choice == 2:
        name = input("Enter the name: ")
        contact = input("Enter the contact: ")
        city = input("Enter the city: ")
        account = input("Enter the account no: ")
        b = {name, contact, city, account}   # storing user info in set_b

    # Print both sets
    elif choice == 3:
        print("set_a:", a)      
        print("set_b:", b)      

    # Union of sets (all unique values)
    elif choice == 4:
       c = a | b       
       print("Combination of set_a and set_b:", c)

    # Intersection of sets (common values)
    elif choice == 5:
       c = a & b 
       print("Common values between both sets:", c)       

    # Difference of sets (values only in set_a)
    elif choice == 6:
       c = a - b 
       print("Values present only in set_a:", c)

    # Exit the program
    else:
        print("Exit")
        break
