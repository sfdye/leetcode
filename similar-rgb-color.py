class Solution:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """

        def closet(s):
            return min(
                ["00", "11", "22", "33", "44", "55", "66", "77", "88", "99", "aa", "bb", "cc", "dd", "ee", "ff"],
                key=lambda x: abs(int(x, 16) - int(s, 16)),
            )

        return "#" + "".join([closet(color[i : i + 2]) for i in range(1, len(color), 2)])
