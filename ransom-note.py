class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        return not collections.Counter(ransomNote) - collections.Counter(magazine)
