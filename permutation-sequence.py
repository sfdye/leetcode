class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = [1]
        for i in range(1, n):
            fact += (fact[-1] * i,)
        k -= 1
        nums = list(i + 1 for i in range(n))
        ans = ""
        for i in range(n - 1, -1, -1):
            q, k = divmod(k, fact[i])
            ans += str(nums[q])
            del nums[q]
        return ans

