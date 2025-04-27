class BankAccount():
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, count):
        if 0 < count:
            self.__balance += count

    def withrout(self, count):
        if count < self.__balance:
            self.__balance -= count


if __name__ == '__main__':
    account = BankAccount(5000)
    print(account.balance)
    account.deposit(1000)
    print(account.balance)
    account.withrout(800)
    print(account.balance)
