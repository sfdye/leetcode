class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        return "".join(k * v for k, v in collections.Counter(s).most_common())
