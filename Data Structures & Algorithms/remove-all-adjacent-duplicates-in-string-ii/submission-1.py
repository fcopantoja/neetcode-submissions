class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # char, count

        for ch in s:
            if not stack or ch != stack[-1][0]:
                stack.append([ch, 1])
            elif ch == stack[-1][0]:
                count = stack[-1][1]
                if count + 1 == k:
                    stack.pop()
                else:
                    stack[-1][1] = count + 1


        return "".join([x[0] * x[1] for x in stack])