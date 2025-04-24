class Soda:
    def __init__(self, ingredient=None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def show_my_drink(self):
        if self.ingredient:
            print(f"Газировка и {self.ingredient}")
        else:
            print("Обычная газировка")


if __name__ == "__main__":
    soda = Soda()
    soda.show_my_drink()

    second_soda = Soda('Кола')
    second_soda.show_my_drink()
