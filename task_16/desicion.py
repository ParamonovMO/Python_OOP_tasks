class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def write(self, text: str):
        with open(self.filename, 'w') as f:
            f.write(text)

    def read(self):
        with open(self.filename, 'r') as f:
            return f.read()


if __name__ == '__main__':
    fm = FileManager("test.txt")
    fm.write("Hello, World!")
    print(fm.read())
