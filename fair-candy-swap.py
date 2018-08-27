class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA, sumB = sum(A), sum(B)
        setA, setB = set(A), set(B)

        avg = (sumA + sumB) // 2
        for x in setA:
            y = x + avg - sumA
            if y in setB:
                return [x, y]
