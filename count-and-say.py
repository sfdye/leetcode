class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        s = '1'
        for i in xrange(n-1):
            l = len(s)
            j = 0
            next_s = ''
            while (j < l):
                count = 1
                while (j < l-1 and s[j] == s[j+1]):
                    j += 1
                    count += 1

                next_s += str(count) + s[j]
                j += 1

            s = next_s

        return s
