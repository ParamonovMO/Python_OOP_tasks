class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def info(self):
        return f"{super().info()} Топливо {self.fuel_type}"


if __name__ == '__main__':
    car = Car('Volkswagen', 'Passat', 'Бензин')
    print(car.info())
