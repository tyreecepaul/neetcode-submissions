class MinStack:

    def __init__(self):
        self.minStack = [] # (val, minVal)

    # check if val < minVal
    def push(self, val: int) -> None:
        minVal = val if not self.minStack else min(val, self.minStack[-1][1])
        self.minStack.append((val, minVal))

    def pop(self) -> None:
        self.minStack.pop()

    def top(self) -> int:
        val, _ = self.minStack[-1]
        return val

    def getMin(self) -> int:
        _, minVal = self.minStack[-1]
        return minVal
