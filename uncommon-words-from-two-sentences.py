class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        counter = collections.Counter()
        counter.update(A.split())
        counter.update(B.split())
        return [k for k, v in counter.items() if v == 1]
