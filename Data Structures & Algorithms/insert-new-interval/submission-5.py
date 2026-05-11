import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = bisect.bisect_left(intervals, newInterval)
        
        intervals.insert(idx, newInterval)
        print(intervals)
        

        
        stack = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= stack[-1][1]:
                stack[-1][1] = max(stack[-1][1], intervals[i][1])
            else:
                stack.append(intervals[i])
        
        return stack

