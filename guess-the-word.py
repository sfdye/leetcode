# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """


class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """

        def pair_matches(a, b):
            return sum(i == j for i, j in zip(a, b))

        def most_overlap_word():
            counts = [collections.defaultdict(int) for _ in range(6)]
            for word in candidates:
                for i, c in enumerate(word):
                    counts[i][c] += 1
            return max(candidates, key=lambda x: sum(counts[i][c] for i, c in enumerate(x)))

        candidates = wordlist[:]
        while candidates:
            s = most_overlap_word()
            matches = master.guess(s)
            if matches == 6:
                return
            candidates = [w for w in candidates if pair_matches(s, w) == matches]
