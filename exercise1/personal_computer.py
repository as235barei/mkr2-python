from exercise1.computer import Computer


class PersonalComputer(Computer):
    def __init__(self, cost=None, model=None, year=None, optical_drive=None):
        super().__init__(cost, model, year)
        self.optical_drive = optical_drive

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

    def get_info(self):
        return f"Personal Computer -> {super().get_info()}, Optical Drive: {'Yes' if self.optical_drive else 'No'}"
