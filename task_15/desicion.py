class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product: Product, quantity: int = 1):
        self.items.append((product, quantity))

    def total(self):
        return sum(p.price * q for p, q in self.items)


if __name__ == '__main__':
    cart = Cart()
    cart.add_product(Product("Молоко", 80), 2)
    cart.add_product(Product("Хлеб", 30))
    print(f"Итого: {cart.total()}₽")
