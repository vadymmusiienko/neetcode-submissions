import heapq
class MedianFinder:

    def __init__(self):
        self.left = [] # Max heap
        self.right = [] # Min heap
        self.l_size = 0
        self.r_size = 0


    def addNum(self, num: int) -> None:
        if self.right and num > self.right[0]:
            heapq.heappush(self.right, num)
            self.r_size += 1
        else:
            heapq.heappush(self.left, -num)
            self.l_size += 1
        
        if self.r_size - self.l_size > 1:
            n = heapq.heappop(self.right)
            heapq.heappush(self.left, -n)
            self.r_size -= 1
            self.l_size += 1
        elif self.l_size - self.r_size > 1:
            n = -heapq.heappop(self.left)
            heapq.heappush(self.right, n)
            self.l_size -= 1
            self.r_size += 1

    def findMedian(self) -> float:
        if self.l_size > self.r_size:
            # Odd
            return -self.left[0]

        if self.r_size > self.l_size:
            # Odd
            return self.right[0]

        first = -self.left[0]
        second = self.right[0]
        return (first + second) / 2