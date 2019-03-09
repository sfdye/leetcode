class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        for i in range(len(num) // 2 + 1):
            if num[i] + num[~i] not in ["00", "11", "88", "69", "96"]:
                return False
        return True

