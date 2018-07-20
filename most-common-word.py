import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = re.findall(r'\w+', paragraph.lower())
        counter = Counter(words)
        for word in banned:
            counter[word] = 0
        return counter.most_common()[0][0]
