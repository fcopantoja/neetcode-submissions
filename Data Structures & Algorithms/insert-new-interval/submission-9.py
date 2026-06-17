class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        l, r = 0, len(intervals) - 1
        while l <= r:
            mid = (l + r) // 2
            if intervals[mid][0] > newInterval[0]:
                r = mid - 1
            else:
                l = mid + 1

        intervals.insert(l, newInterval)
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(intervals[i][1], result[-1][1])
            else:
                result.append(intervals[i])

        return result