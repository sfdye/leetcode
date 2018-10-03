class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def find_kth(a, b, k):
            if not a:
                return b[k]
            if not b:
                return a[k]
            ia = len(a) // 2
            ib = len(b) // 2
            ma = a[ia]
            mb = b[ib]
            if ia + ib < k:
                if ma > mb:
                    return find_kth(a, b[ib + 1 :], k - ib - 1)
                else:
                    return find_kth(a[ia + 1 :], b, k - ia - 1)
            else:
                if ma > mb:
                    return find_kth(a[:ia], b, k)
                else:
                    return find_kth(a, b[:ib], k)

        l = len(nums1) + len(nums2)
        if l & 1:
            return find_kth(nums1, nums2, l // 2)
        else:
            return (find_kth(nums1, nums2, l // 2 - 1) + find_kth(nums1, nums2, l // 2)) / 2
