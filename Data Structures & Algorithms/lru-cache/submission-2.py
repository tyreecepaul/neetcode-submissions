class Node:
    def __init__(self, key: None, val: None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        
        self.cache = {}
        self.cap = capacity  
        
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _delete(self, node):
        prev, nxt = node.prev, node.next
        prev.next = node.next
        nxt.prev = node.prev

    def _insert(self, node):
        prev = self.head
        nxt = self.head.next

        prev.next = node
        nxt.prev = node

        node.prev = prev
        node.next = nxt

    # return val else return -1
    def get(self, key: int) -> int:
        if key in self.cache:
            self._delete(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1        

    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            self._delete(self.cache[key])
        self.cache[key] = Node(key, val)
        self._insert(self.cache[key])
                 
        if len(self.cache) > self.cap:
            temp = self.tail.prev 
            self._delete(temp)
            del self.cache[temp.key]
        

