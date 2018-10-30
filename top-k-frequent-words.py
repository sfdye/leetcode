class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        feq = collections.defaultdict(list)
        for key, count in collections.Counter(nums).items():
            feq[count].append(key)
        res = []
        for i in range(len(nums) + 1, -1, -1):
            res.extend(feq[i])
            if len(res) >= k:
                break
        return res[:k]
