class Computer:
    def __init__(self, cost=None, model=None, year=None):
        self.cost = cost
        self.model = model
        self.year = year

    def set_params(self):
        while True:
            try:
                cost = float(input("Enter cost: "))
                if cost < 0:
                    raise ValueError("Cost cannot be negative.")
                self.cost = cost
                break
            except ValueError as e:
                print(e)

        self.model = input("Enter model: ")

        while True:
            try:
                year = int(input("Enter year (2000-2024): "))
                if year < 2000 or year > 2024:
                    raise ValueError("Year must be between 2000 and 2024.")
                self.year = year
                break
            except ValueError as e:
                print(e)

    def get_info(self):
        return f"Model: {self.model}, Year: {self.year}, Cost: ${self.cost}"
