contacts = {}

def show_menu():
    print("\n Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1–5): ")

    if choice == '1':
        name = input("Enter name: ")1
    
        number = input("Enter number: ")
        contacts[name] = number
        print("Contact added!")

    elif choice == '2':
        if contacts:
            print("\n All Contacts:")
            for name, number in contacts.items():
                print(f"{name} → {number}")
        else:
            print("No contacts to show.")

    elif choice == '3':
        search = input("Enter name to search: ")
        if search in contacts:
            print(f" Found: {search} → {contacts[search]}")
        else:
            print(" Contact not found.")

    elif choice == '4':
        delete = input("Enter name to delete: ")
        if delete in contacts:
            del contacts[delete]
            print(f" {delete} deleted.")
        else:
            print(" Contact not found.")

    elif choice == '5':
        print(" Exiting Contact Book. Goodbye!")
        break

    else:
        print(" Invalid choice. Please enter a number from 1–5.")
