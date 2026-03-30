class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        """if not intervals:
            intervals.append(newInterval)
        else:
            for i in range(1, len(intervals)):
                if intervals[i][0] > newInterval[0]:
                    intervals.insert(i, newInterval)
                    break
        """
        
        print(intervals)
        stack = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= stack[-1][1]:
                stack[-1][1] = max(stack[-1][1], intervals[i][1])
            else:
                stack.append(intervals[i])
        
        return stack

