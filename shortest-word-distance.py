class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        p1, p2 = [], []
        for i, word in enumerate(words):
            if word == word1:
                p1.append(i)
            if word == word2:
                p2.append(i)
        return min(abs(i - j) for i in p1 for j in p2)
