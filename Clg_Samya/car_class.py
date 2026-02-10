class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_description(self):
        return f"{self.year} {self.make} {self.model}"
    
my_car = Car("MG", "Hector", 2025)
print(my_car.get_description())