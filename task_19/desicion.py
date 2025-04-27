class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return 'Gav'


class Cat(Animal):
    def speak(self):
        return 'Meow'


if __name__ == '__main__':
    dog = Dog()
    dog.speak()
    cat = Cat()
    cat.speak()
