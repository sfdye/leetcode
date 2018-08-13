class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        if len(s) < len(p):
            return []

        p_counter = collections.Counter({x: 0 for x in string.ascii_lowercase})
        p_counter.update(p)
        window_size = len(p)
        ans = []
        s_counter = collections.Counter({x: 0 for x in string.ascii_lowercase})
        s_counter.update(s[:window_size])

        if s_counter == p_counter:
            ans.append(0)
        for i in range(1, len(s) - window_size + 1):
            left, right = i, i + window_size - 1
            s_counter[s[left - 1]] -= 1
            s_counter[s[right]] += 1
            if s_counter == p_counter:
                ans.append(left)

        return ans
