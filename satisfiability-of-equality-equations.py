class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(u):
            if p[u] != u:
                p[u] = find(p[u])
            return p[u]

        p = {a: a for a in string.ascii_lowercase}
        for a, c, _, b in equations:
            if c == "=":
                p[find(b)] = p[find(a)]
        return not any(find(a) == find(b) for a, c, _, b in equations if c == "!")

