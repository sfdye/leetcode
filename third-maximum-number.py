class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        m = [-float("inf")] * 3
        for n in nums:
            if n not in m:
                if n > m[0]:
                    m = [n, m[0], m[1]]
                elif n > m[1]:
                    m = [m[0], n, m[1]]
                elif n > m[2]:
                    m = [m[0], m[1], n]
        return max(m) if -float("inf") in m else m[2]
