import utils

def menu():
    print("\n=== NEON CLI TOOL ===")
    print("1. System Info")
    print("2. Generate Password")
    print("3. Random Joke")
    print("4. Exit")

while True:
    menu()
    choice = input("\nSelect option: ")

    if choice == "1":
        utils.system_info()

    elif choice == "2":
        length = int(input("Password length: "))
        print("Generated Password:", utils.generate_password(length))

    elif choice == "3":
        print("Joke:", utils.get_joke())

    elif choice == "4":
        print("Exiting... 👋")
        break

    else:
        print("Invalid option")
