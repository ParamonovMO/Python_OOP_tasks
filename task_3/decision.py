# РЕШЕНИЕ БЕЗ ИНКАПСУЛЯЦИИ 
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Счет пополнен на {amount}₽. Текущий баланс: {self.balance}₽")
        else:
            print("Ошибка: сумма для пополнения должна быть положительной.")

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f"Снято {amount}₽. Остаток на счете: {self.balance}₽")
        else:
            print("Сумма снятия не должна быть больше баланса")

    def __str__(self):
        return f"Владелец счета {self.owner}, на его счету {self.balance}"


if __name__ == "__main__":
    owner = BankAccount('Maxim', 1000)
    owner.deposit(500)
    owner.withdraw(600)
    print(owner)
    owner.deposit(-100)
    owner.withdraw(10000)