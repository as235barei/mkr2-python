from exercise1.laptop import Laptop
from exercise1.personal_computer import PersonalComputer
from exercise1.server import Server


def main():
    computers = []

    while True:
        print("\nMenu:")
        print("1. Add Laptop")
        print("2. Add Personal Computer")
        print("3. Add Server")
        print("4. Display All Computers")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            laptop = Laptop()
            laptop.set_params()
            computers.append(laptop)
        elif choice == 2:
            pc = PersonalComputer()
            pc.set_params()
            computers.append(pc)
        elif choice == 3:
            server = Server()
            server.set_params()
            computers.append(server)
        elif choice == 4:
            if not computers:
                print("No computers to display.")
            else:
                for computer in computers:
                    print(computer.get_info())
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")


main()
