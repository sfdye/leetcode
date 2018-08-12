class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """

        words = S.split()
        ans = []
        suffix = ""
        for word in words:
            if word[0].lower() in "aeiou":
                word += "ma"
            else:
                word = word[1:] + word[0] + "ma"
            suffix += "a"
            word += suffix
            ans.append(word)

        return " ".join(ans)
