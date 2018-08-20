class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        return [k for k, _ in sorted(collections.Counter(words).items(), key=lambda x: (-x[1], x[0]))][:k]
