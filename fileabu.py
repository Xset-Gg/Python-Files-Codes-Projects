class Car:
    def __init__(self, brand, model, year,color, for_sale):
        self.brand = brand
        self.model = model
        self.year = year
        self.color =color
        self.for_sale = for_sale

car1 = Car("Ford", "Mustang", 2024, False)
car2 = Car("Ford", "Corvette", 2025, True)
car3 = Car("Ford", "Charger", 2026, True)

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)