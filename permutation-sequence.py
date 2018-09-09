class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k -= 1
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[-1] * i)
        nums = list(range(1, n + 1))
        ans = ""
        while n:
            n -= 1
            i, k = divmod(k, factorial[n])
            ans += str(nums[i])
            del nums[i]
        return ans
