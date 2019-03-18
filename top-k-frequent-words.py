class Solution:
    def topKFrequent(self, nums, k):
        def quick_select(l, r):
            if l >= r:
                return
            pivot = random.randint(l, r)
            counts[l], counts[pivot] = counts[pivot], counts[l]
            i = l
            for j in range(l + 1, r + 1):
                if counts[j][1] > counts[l][1]:
                    i += 1
                    counts[i], counts[j] = counts[j], counts[i]
            counts[l], counts[i] = counts[i], counts[l]
            if i + 1 == k:
                return
            elif i + 1 < k:
                quick_select(i + 1, r)
            else:
                quick_select(l, i - 1)

        counts = list(collections.Counter(nums).items())
        quick_select(0, len(counts) - 1)
        return [c[0] for c in counts[:k]]
