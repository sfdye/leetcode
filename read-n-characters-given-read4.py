# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):


class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        count = 0
        buf4 = [""] * 4
        while n > 0:
            now = min(n, read4(buf4))
            if now == 0:
                break
            buf[count : count + now] = buf4[: now]
            count += now
            n -= now
        return count
