class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join(filter(lambda x: x.strip() != '', s.split(' ')[::-1]))
