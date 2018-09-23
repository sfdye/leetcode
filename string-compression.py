class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        anchor = write = 0
        for read, c in enumerate(chars):
            if read == len(chars) - 1 or c != chars[read + 1]:
                chars[write] = chars[anchor]
                write += 1
                count = read - anchor + 1
                if count > 1:
                    for d in str(count):
                        chars[write] = d
                        write += 1
                anchor = read + 1
        return write

