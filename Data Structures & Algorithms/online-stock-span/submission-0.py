"""
span is the max number of consective days in which a stock has been >= the current day


"""

class StockSpanner:

    def __init__(self):
        # Stack stores pairs of (price, span)
        self.stack = []
        
    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        
        self.stack.append((price, span))
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)