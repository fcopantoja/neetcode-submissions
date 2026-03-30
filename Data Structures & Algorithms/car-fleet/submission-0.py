class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(p, r) for p, r in zip(position, speed)]
        arr.sort()
        stack = []
        
        for ps, sp in reversed(arr):
            t = (target - ps) / sp
            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
            


