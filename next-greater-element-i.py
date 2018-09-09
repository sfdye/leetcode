class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = {}
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            while stack and nums2[i] >= stack[-1]:
                stack.pop()
            if stack:
                res[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        return [res.get(num, -1) for num in nums1]
