class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        def construct_dict(wordList):
            d = collections.defaultdict(list)
            for word in wordList:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i + 1 :]
                d[s].append(word)
            return d

        queue = collections.deque([(beginWord, 1)])
        d = construct_dict(wordList)
        visited = set()
        while queue:
            cur, step = queue.popleft()
            visited.add(cur)
            if cur == endWord:
                return step
            for i in range(len(word)):
                s = word[:i] + "_" + word[i + 1]
                for neigh in d[s]:
                    if neigh not in visited:
                        queue.append((neigh, step + 1))

        return 0
