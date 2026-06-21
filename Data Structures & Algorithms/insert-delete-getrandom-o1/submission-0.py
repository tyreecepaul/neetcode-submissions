class RandomizedSet:

    def __init__(self):
        self.data = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        self.data[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data:
            return False
        index = self.data[val]
        last = self.nums[-1]
        self.nums[index] = last
        self.data[last] = index
        self.nums.pop()
        del self.data[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
    

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()