class Solution:
    def validWordAbbreviation(self, word: "str", abbr: "str") -> "bool":
        i = j = 0
        while i < len(word) and j < len(abbr):
            if abbr[j].islower() and word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isdigit():
                if abbr[j] == "0":
                    return False
                k = 0
                while j < len(abbr) and abbr[j].isdigit():
                    k = k * 10 + int(abbr[j])
                    j += 1
                i += k
            else:
                break

        return i == len(word) and j == len(abbr)
