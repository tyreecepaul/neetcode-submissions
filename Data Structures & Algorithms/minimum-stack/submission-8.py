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
        return self.minStack[-1][0]
        

    def getMin(self) -> int:
        return self.minStack[-1][1]
