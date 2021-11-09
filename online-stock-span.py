class StockSpanner:

    def __init__(self):
        self.lt = []
        self.c = -1

    def next(self, price: int) -> int:
        self.c = self.c + 1

        while self.lt and self.lt[-1][0] <= price:
            self.lt.pop()
        if len(self.lt) == 0:
            self.lt.append((price, self.c))
            return self.c + 1
        else:
            x = self.lt[-1][1]
            self.lt.append((price, self.c))
            return self.c - x

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)