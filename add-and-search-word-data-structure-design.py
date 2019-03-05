class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        TrieNode = lambda: collections.defaultdict(TrieNode)
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie
        for c in word:
            node = node[c]
        node["$"] = None

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self._search(self.trie, word)

    def _search(self, node, word):
        if not word:
            return "$" in node
        else:
            if word[0] == ".":
                return any(self._search(child, word[1:]) for child in node.values() if child)
            else:
                return word[0] in node and self._search(node[word[0]], word[1:])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
