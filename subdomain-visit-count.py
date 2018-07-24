from collections import Counter


class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """

        counter = Counter()

        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            parts = domain.split(".")
            for i in range(len(parts)):
                counter[".".join([parts[i:]])] += int(count)
        return ["{} {}".format(v, k) for k, v in counter.items()]
 