class Solution:
    def containsNearbyAlmostDuplicate(self, nums: "List[int]", k: "int", t: "int") -> "bool":
        if t < 0:
            return False
        w = t + 1
        d = {}
        for i in range(len(nums)):
            m = nums[i] // w
            if m in d:
                return True
            elif m - 1 in d and abs(d[m - 1] - nums[i]) < w:
                return True
            elif m + 1 in d and abs(d[m + 1] - nums[i]) < w:
                return True
            d[m] = nums[i]
            if i >= k:
                del d[nums[i - k] // w]
        return False
