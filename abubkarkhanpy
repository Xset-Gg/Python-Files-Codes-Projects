class FriendlyCalculator:
    def __init__(self, user_name):
        # Initializing attributes (jo data hamari class yaad rakhegi)
        self.owner = user_name
        self.history = []
        print(f"Hey {self.owner}! Main aapka personal calculator hoon. Chaliye hisab shuru karte hain! 🚀")

    def add(self, a, b):
        result = a + b
        self.history.append(f"Added {a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"Subtracted {a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"Multiplied {a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            return "Oho! Zero (0) se divide nahi kar sakte, math ro padega! 😢"
        result = a / b
        self.history.append(f"Divided {a} / {b} = {result}")
        return result

    def show_history(self):
        print(f"\n--- {self.owner}'s Calculation History ---")
        if not self.history:
            print("Abhi tak koi calculation nahi ki!")
        else:
            for index, calculation in enumerate(self.history, 1):
                print(f"{index}. {calculation}")