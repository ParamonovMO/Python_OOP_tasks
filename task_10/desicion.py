class Animal:
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return 'ГАВ'


class Cat(Animal):
    def sound(self):
        return 'Мяу'


if __name__ == '__main__':
    animals = [Dog(), Cat()]
    for animal in animals:
        print(animal.sound())
