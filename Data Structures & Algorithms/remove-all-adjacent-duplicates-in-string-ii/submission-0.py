class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for ch in s:
            has_group = False

            if stack and len(stack) >= (k - 1):
                j = -1
                has_group = True
                count = 1
                while count < k:
                    if stack[j] == ch:
                        j -= 1
                        count += 1
                    else:
                        has_group = False
                        break

                if has_group:
                    for i in range(k - 1):
                        stack.pop()

            if not has_group:
                stack.append(ch)

        return "".join(stack)
        