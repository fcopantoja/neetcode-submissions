class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 1

        if len(tokens) == 1:
            return int(tokens[0])

        for token in tokens:
            if token == "+":
                b = stack.pop()
                a = stack.pop()
                result = a + b
                stack.append(result)
            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                result = a - b
                stack.append(result)
            elif token == "*":
                b = stack.pop()
                a = stack.pop()
                result = a * b
                stack.append(result)
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                result = int(a / b)
                stack.append(result)
            else:
                stack.append(int(token))

        return result
