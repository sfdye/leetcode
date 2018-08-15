class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        digits[len(digits) - 1] += 1
        x = len(digits) - 1
        while x > 0 and digits[x] == 10:
            digits[x - 1] += 1
            digits[x] = 0
            x -= 1

        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)

        return digits
