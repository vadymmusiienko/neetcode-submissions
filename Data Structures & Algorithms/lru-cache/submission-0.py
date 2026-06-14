import heapq
class LRUCache:

    class Node:
        def __init__(self, key, val, next=None, prev=None):
            self.key = key
            self.val = val
            self.next = next
            self.prev = prev
    

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0

        # Key-pointer pairs
        self.cache = {}
        
        # LRU pairs (key, value nodes with prev and next)
        # Doubly linked list (Always has 2 nodes)
        self.head = self.Node(0, 0) # MRU
        self.tail = self.Node(0, 0) # LRU
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    # Inserts at head
    def insert(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.remove(self.cache[key])
        self.insert(self.cache[key])

        return self.cache[key].val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.size -= 1

        new_node = self.Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)
        self.size += 1

        if self.size > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]
            self.size -= 1
        
