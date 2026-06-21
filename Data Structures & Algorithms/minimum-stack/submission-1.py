class MinStack:

    def __init__(self):
        self.stack = []
        self.minValue = None
        

    def push(self, val: int) -> None:
        if self.minValue == None or val < self.minValue:
            self.minValue = val
        self.stack.append(val)
        
    def pop(self) -> None:
        if not self.stack:
            return
        val = self.stack.pop()
        if val == self.minValue:
            self.minValue = min(self.stack) if self.stack else None
        
    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.minValue

        
