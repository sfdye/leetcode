class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.root = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node[None] = None

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """

        def find(word, node):
            if not word:
                return None in node
            for ch in word:
                if ch != ".":
                    return ch in node and find(word[1:], node[ch])
                else:
                    return any(
                        find(word[1:], child) for child in node.values() if child
                    )

        return find(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
