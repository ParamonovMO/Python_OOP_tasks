class Library:
    def __init__(self):
        self.books = []

    def add_book(self, *args):
        self.books.append(*args)

    def show_book(self):
        for i in self.books:
            print(i)


if __name__ == '__main__':
    library = Library()
    library.add_book(('Мастер и Маргарита", "Булгаков", 1966'))
    library.add_book(('"Преступление и наказание", "Достоевский", 1866'))
    library.show_book()
