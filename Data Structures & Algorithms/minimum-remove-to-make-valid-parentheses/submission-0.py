class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        arr = list(s)
        stack = []

        for i, ch in enumerate(arr):
            if ch not in ("(", ")"):
                continue
            
            if ch == "(":
                stack.append(("(", i))
            else:
                if not stack:
                    arr[i] = ""
                elif stack[-1][0] == "(":
                    stack.pop()
                else:
                    arr[i] = ""

        while stack:
            val, idx = stack.pop()
            arr[idx] = ""

        
        return "".join(arr)
            