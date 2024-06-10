from exercise1.computer import Computer


class Laptop(Computer):
    def __init__(self, cost=None, model=None, year=None, screen_size=None):
        super().__init__(cost, model, year)
        self.screen_size = screen_size

    def set_params(self):
        super().set_params()
        while True:
            try:
                screen_size = float(input("Enter screen size: "))
                if screen_size < 0:
                    raise ValueError("Screen size cannot be negative.")
                self.screen_size = screen_size
                break
            except ValueError as e:
                print(e)

    def get_info(self):
        return f"Laptop -> {super().get_info()}, Screen Size: {self.screen_size}\""
