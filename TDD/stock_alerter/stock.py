# this is a simple example using TDD


class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.price = None

    def update(self, timestamp, price):
        if price < 0:
            raise ValueError("Price Should not be negative")
        self.price = price