class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1 = m2 = m3 = -float("inf")
        for num in nums:
            if num > m1:
                m1, m2, m3 = num, m1, m2
            elif m2 < num < m1:
                m2, m3 = num, m2
            elif m3 < num < m2:
                m3 = num
        return m3 if m3 > -float("inf") else m1
