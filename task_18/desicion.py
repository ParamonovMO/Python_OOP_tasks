class Car:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year


if __name__ == '__main__':
    car = Car('Volkswagen', 'Passat', 2012)
    print(car.mark)
    print(car.model)
    print(car.year)
