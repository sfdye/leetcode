class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        for row in A:
            l = len(row)
            for i in range(l//2):
                row[i], row[l-i-1] = row[l-i-1], row[i]
            for i in range(l):
                row[i] = 1 - row[i]
                
        return A
