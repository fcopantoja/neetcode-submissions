class MedianFinder:
    def __init__(self):
        self.smallest = []
        self.largest = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallest, -num)

        if (
            self.largest and
            -self.smallest[0] > self.largest[0]
        ):
            val = heapq.heappop(self.smallest)
            heapq.heappush(self.largest, -val)

        if len(self.largest) > len(self.smallest) + 1:
            val = heapq.heappop(self.largest)
            heapq.heappush(self.smallest, -val)

        if len(self.smallest) > len(self.largest) + 1:
            val = heapq.heappop(self.smallest)
            heapq.heappush(self.largest, -val)



    def findMedian(self) -> float:
        if len(self.smallest) == len(self.largest):
            v1 = self.smallest[0] * -1
            v2 = self.largest[0]
            return (v1 + v2) / 2
        elif len(self.smallest) > len(self.largest):
            return -self.smallest[0]
        elif len(self.smallest) < len(self.largest):
            return self.largest[0]