class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        nums1 = list(map(int, version1.split(".")))
        nums2 = list(map(int, version2.split(".")))

        for x, y in itertools.zip_longest(nums1, nums2, fillvalue=0):
            if x != y:
                return [-1, 1][x > y]
        return 0
