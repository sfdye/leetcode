class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        def self_dividing(n):
            for c in str(n):
                if int(c) == 0:
                    return False
                if n % int(c) != 0:
                    return False
            return True

        ans = []
        for num in range(left, right + 1):
            if self_dividing(num):
                ans.append(num)
        return ans
