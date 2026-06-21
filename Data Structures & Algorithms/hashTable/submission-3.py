class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * self.capacity
    
    def hash_fn(self, key: int):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        idx = self.hash_fn(key)
        node = self.table[idx]

        if not node:
            self.table[idx] = Node(key, value)
            self.size += 1
        else:
            prev = None
            while node:
                if node.key == key:
                    node.value = value
                    return
                prev, node = node, node.next
            prev.next = Node(key, value)
            self.size += 1

        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        idx = self.hash_fn(key)
        node = self.table[idx]

        while node:
            if node.key == key:
                return node.value
            node = node.next

        return -1

    def remove(self, key: int) -> bool:
        idx = self.hash_fn(key)
        node = self.table[idx]
        prev = None

        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[idx] = node.next
                self.size -= 1
                return True
            prev, node = node, node.next
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0

        for node in old_table:
            while node:
                self.insert(node.key, node.value)
                node = node.next