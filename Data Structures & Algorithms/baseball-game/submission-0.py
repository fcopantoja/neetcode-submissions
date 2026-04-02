class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        curr_sum = 0

        for operation in operations:
            if operation == "+":
                a = stack[-1]
                b = stack[-2]
                stack.append(a + b)
                curr_sum += a + b
            elif operation == "C":
                a = stack.pop()
                curr_sum -= a
            elif operation == "D":
                a = stack[-1] * 2
                stack.append(a)
                curr_sum += a
            else:
                a = int(operation)
                stack.append(a)
                curr_sum += a
        
        return curr_sum
        return sum(stack)