class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i2 = i3 = i5 = 0
        ans = [1]
        for _ in range(n - 1):
            m = min(ans[i2] * 2, ans[i3] * 3, ans[i5] * 5)
            if m == ans[i2] * 2:
                i2 += 1
            if m == ans[i3] * 3:
                i3 += 1
            if m == ans[i5] * 5:
                i5 += 1
            ans.append(m)
        return ans[-1]
