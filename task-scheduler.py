class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = list(collections.Counter(tasks).values())
        m = max(c)
        mc = c.count(m)
        return max(len(tasks), (m - 1) * (n + 1) + mc)
