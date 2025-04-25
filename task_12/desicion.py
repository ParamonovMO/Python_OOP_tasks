class Bank:
    def __init__(self):
        self.transaction = []

    def add_transaction(self, amount):
        self.transaction.append(amount)

    def balance(self):
        return sum(self.transaction)


if __name__ == '__main__':
    bank = Bank()
    bank.add_transaction(1000)
    bank.add_transaction(-500)
    print(f"Баланс: {bank.balance()}")
