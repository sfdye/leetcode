class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        TrieNode = lambda: collections.defaultdict(TrieNode)
        self.trie = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.trie
        for c in word:
            node = node[c]
        node["#"] = None

    def find(self, node, word):
        if not word:
            return "#" in node
        else:
            for c in word:
                if c != ".":
                    return c in node and self.find(node[c], word[1:])
                else:
                    return any(self.find(child, word[1:]) for child in node.values() if child)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.find(self.trie, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
