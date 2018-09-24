class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = "-" if numerator * denominator < 0 else ""
        ans = [sign + str(n), "."]
        stack = []
        while remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(abs(remainder) * 10, abs(denominator))
            ans.append(str(n))
        idx = stack.index(remainder)
        ans.insert(idx + 2, "(")
        ans.append(")")
        return "".join(ans).replace("(0)", "").rstrip(".")
