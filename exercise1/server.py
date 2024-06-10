from exercise1.computer import Computer


class Server(Computer):
    def __init__(self, cost=None, model=None, year=None, optical_drive=None, server_type=None):
        super().__init__(cost, model, year)
        self.optical_drive = optical_drive
        self.server_type = server_type

    def set_params(self):
        super().set_params()
        while True:
            try:
                choice = int(input("Has optical drive? (1 - yes / 2 - no): "))
                if choice in (1, 2):
                    self.optical_drive = (choice == 1)
                    break
                else:
                    print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        while True:
            try:
                choice = int(input("Enter server type (1 - cabinet / 2 - floor): "))
                if choice == 1:
                    self.server_type = "cabinet"
                    break
                elif choice == 2:
                    self.server_type = "floor"
                    break
                else:
                    print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_info(self):
        return f"Server -> {super().get_info()}, Optical Drive: {'Yes' if self.optical_drive else 'No'}, Type: {self.server_type}"
