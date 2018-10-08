class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        TrieNode = lambda: collections.defaultdict(TrieNode)
        self.trie = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.trie
        for c in word:
            node = node[c]
        node["#"] = "#"

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.trie
        for c in word:
            if c not in node:
                return False
            else:
                node = node[c]
        return "#" in node

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.trie
        for c in prefix:
            if c not in node:
                return False
            else:
                node = node[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
