class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = sorted(map(str, nums), key=LargerNumKey)
        return "".join(nums) if nums[0] != "0" else "0"
