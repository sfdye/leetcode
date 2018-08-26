class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        return ["{}:{:02d}".format(h, m) for h in range(12) for m in range(60) if (bin(h) + bin(m)).count("1") == num]
