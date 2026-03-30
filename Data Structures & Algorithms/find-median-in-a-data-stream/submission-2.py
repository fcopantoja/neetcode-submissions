import heapq

class MedianFinder:

    def __init__(self):
        self.left = [] # maxheap
        self.right = [] # minheap

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.left, num)

        if (
            self.left and self.right and
            self.left[0] > self.right[0]
        ):
            val = heapq.heappop_max(self.left)
            heapq.heappush(self.right, val)

        if len(self.left) > (len(self.right) + 1):
            val = heapq.heappop_max(self.left)
            heapq.heappush(self.right, val)

        if len(self.right) > len(self.left) + 1:
            val = heapq.heappop(self.right)
            heapq.heappush_max(self.left, val)

        print(self.left, self.right)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return self.left[0]
        elif len(self.left) < len(self.right):
            return self.right[0]

        return (self.left[0] + self.right[0]) / 2
        
        