class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(pos, sp) for pos, sp in zip(position, speed)]
        arr.sort()
        stack = []

        for pos, spee in reversed(arr):
            time = (target - pos) / spee
            stack.append(time)
            
            if len(stack) > 1 and time <= stack[-2]:
                stack.pop()
                    

        return len(stack)

        