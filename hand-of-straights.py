class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if W == 0:
            return False
        if W > len(hand) or len(hand) % W != 0:
            return False
        c = collections.Counter(hand)
        for i in sorted(c):
            if c[i] > 0:
                cur = c[i]
                for j in range(W):
                    c[i + j] -= cur
                    if c[i + j] < 0:
                        return False
        return True
