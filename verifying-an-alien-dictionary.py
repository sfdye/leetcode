class Solution:
    def isAlienSorted(self, words: "List[str]", order: "str") -> "bool":
        order_dict = {c: i for i, c in enumerate(order)}

        def less(a, b):
            for i in range(min(len(a), len(b))):
                if order_dict[a[i]] < order_dict[b[i]]:
                    return True
                elif order_dict[a[i]] > order_dict[b[i]]:
                    return False
            return len(a) < len(b)

        return all(less(words[i], words[i + 1]) for i in range(len(words) - 1))

