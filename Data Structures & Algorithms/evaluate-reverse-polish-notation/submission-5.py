class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        res = 0

        for t in tokens:
            if t in operators:
                right = int(stack.pop())
                left = int(stack.pop())

                if t == '+':
                    res = left + right
                elif t == '-':
                    res = left - right
                elif t == '*':
                    res = left * right
                elif t =='/':
                    res = left / right

                stack.append(res)

            else:
                stack.append(t)

        return int(stack[0])
            
        