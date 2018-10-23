class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """

        def isomorphic(word):
            return len(word) == len(pattern) and len(set(word)) == len(set(pattern)) == len(set(zip(word, pattern)))

        return list(filter(isomorphic, words))
