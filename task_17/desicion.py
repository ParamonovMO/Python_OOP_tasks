class Ticket:
    def __init__(self, number: int):
        self.number = str(number)

    def is_lucky(self) -> bool:
        return (sum(map(int, self.number[:3])) == sum(map(int, self.number[3:])))


if __name__ == '__main__':
    ticket = Ticket(123321)
    print(ticket.is_lucky())
