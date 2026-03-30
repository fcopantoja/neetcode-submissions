class MedianFinder:

    def __init__(self):
        self.nums = []
        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()
        

    def findMedian(self) -> float:
        if len(self.nums) % 2 != 0:
            return self.nums[len(self.nums) // 2]
        else:
            middle = len(self.nums) // 2
            return (self.nums[middle - 1] + self.nums[middle]) / 2
        
        