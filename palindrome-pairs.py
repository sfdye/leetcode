class TrieNode:
    def __init__(self):
        self.idx = -1
        self.palin = []
        self.children = collections.defaultdict(TrieNode)


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        self.root = TrieNode()

        for idx, word in enumerate(words):
            self.add_word(word, idx)

        res = []
        for idx, word in enumerate(words):
            self.search_word(word, idx, res)
        return res

    def add_word(self, word, idx):
        node = self.root
        for i, c in enumerate(reversed(word)):
            if self.is_palindrome(word[: len(word) - i]):
                node.palin.append(idx)
            node = node.children[c]
        node.palin.append(idx)
        node.idx = idx

    def search_word(self, word, idx, res):
        node = self.root
        for i, c in enumerate(word):
            if node.idx != -1 and node.idx != idx and self.is_palindrome(word[i:]):
                res.append([idx, node.idx])
            node = node.children.get(c)
            if not node:
                return
        for palin in node.palin:
            if idx != palin:
                res.append([idx, palin])

    def is_palindrome(self, s):
        return s == s[::-1]

