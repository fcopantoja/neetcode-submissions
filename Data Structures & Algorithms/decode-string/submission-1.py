class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                currstring = ""
                while stack and stack[-1] != "[":
                    currstring = stack.pop() + currstring

                stack.pop() # remove open [

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                subs = int(k) * currstring
                for ch2 in subs:
                    stack.append(ch2)
                
                
        return "".join(stack)