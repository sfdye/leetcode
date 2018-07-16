class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        a = map(int, version1.split("."))
        b = map(int, version2.split("."))

        lena = len(a)
        lenb = len(b)
        if lena > lenb:
            b += [0] * (lena-lenb)
        elif lena < lenb:
            a += [0] * (lenb-lena)

        for i in range(min(len(a),len(b))):
            if a[i] > b[i]:
                return 1
            elif a[i] < b[i]:
                return -1

        return 0
