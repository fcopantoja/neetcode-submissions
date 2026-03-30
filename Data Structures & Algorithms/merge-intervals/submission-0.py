class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        stack = [intervals[0]]

        for i in range(1, len(intervals)):
            a = stack[-1]
            if intervals[i][0] <= a[1]:
                a[1] = max(intervals[i][1], a[1])
            else:
                stack.append(intervals[i])

        return stack