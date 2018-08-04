class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        ans = collections.defaultdict(list)
        for s in strs:
            ans["".join(sorted(s))].append(s)

        return list(ans.values())
