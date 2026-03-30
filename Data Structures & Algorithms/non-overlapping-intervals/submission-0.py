class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        stack = [intervals[0]]

        print(intervals)
        for interval in intervals:
            if stack[-1][1] > interval[0]:
                stack[-1][1] = min(stack[-1][1], interval[1])
            else:
                stack.append(interval)
        

        return len(intervals) - len(stack)