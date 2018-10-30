class Solution:
    def topKFrequent(self, nums, k):
        def quick_select(l, r):
            pivot = l
            i, j = l, r
            while i < j:
                while i < j and counts[j][1] <= counts[pivot][1]:
                    j -= 1
                while i < j and counts[i][1] >= counts[pivot][1]:
                    i += 1
                counts[i], counts[j] = counts[j], counts[i]
            counts[l], counts[i] = counts[i], counts[l]

            if i + 1 == k:
                return counts[: i + 1]
            elif i + 1 < k:
                return quick_select(i + 1, r)
            else:
                return quick_select(l, i - 1)

        if not nums:
            return []

        counts = collections.defaultdict(int)
        for num in nums:
            counts[num] += 1
        counts = list(counts.items())
        return [c[0] for c in quick_select(0, len(counts) - 1)]
