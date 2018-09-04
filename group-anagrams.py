class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = collections.defaultdict(list)
        for str in strs:
            d[tuple(sorted(str))].append(str)
        return list(d.values())
