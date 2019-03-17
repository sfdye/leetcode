class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        i1 = i2 = -1
        ans = float("inf")
        for i in range(len(words)):
            if words[i] == word1:
                i1 = i
            elif words[i] == word2:
                i2 = i
            if i1 != -1 and i2 != -1:
                ans = min(ans, abs(i1 - i2))
        return ans

