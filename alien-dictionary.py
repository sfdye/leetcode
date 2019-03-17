class Solution:
    def alienOrder(self, words: List[str]) -> str:
        suc, pre = collections.defaultdict(set), collections.defaultdict(set)
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    suc[a].add(b)
                    pre[b].add(a)
                    break
        chars = set("".join(words))
        queue = collections.deque(chars - set(pre))
        ans = ""
        while queue:
            a = queue.popleft()
            ans += a
            for b in suc[a]:
                pre[b].discard(a)
                if not pre[b]:
                    queue.append(b)
        return ans if chars == set(ans) else ""

