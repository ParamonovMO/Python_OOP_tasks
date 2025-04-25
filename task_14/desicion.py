from random import randint


class Dice:
    def roll(self):
        return randint(1, 6)


if __name__ == '__main__':
    dice = Dice()
    print(f"Выпало: {dice.roll()}")
