class Solution:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.pos = collections.defaultdict(list)
        for index, num in enumerate(nums):
            self.pos[num].append(index)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(self.pos[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
