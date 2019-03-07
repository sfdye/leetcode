class Solution:
    def calculate(self, s: str) -> int:
        stack, sign, num = [], "+", 0
        s += "$"
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-*/$":
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = c
        return sum(stack)
