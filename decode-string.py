class Solution:
    def decodeString(self, s):
        stack, num = [["", 1]], 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + ord(ch) - ord("0")
            elif ch == "[":
                stack.append(["", num])
                num = 0
            elif ch == "]":
                s, k = stack.pop()
                stack[-1][0] += s * k
            else:
                stack[-1][0] += ch
        return stack[0][0]
