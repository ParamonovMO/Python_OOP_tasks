class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f'Книга {self.title} автора {self.author} выпущена в {self.year} году'


if __name__ == "__main__":
    book = Book('1984', 'Джордж Оруэлл', 1949)
    print(book.info())
