class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        a = [1]
        for i in range(2,rowIndex+2):
            b = [0] * i
            for j in range(0,i):
                if j == 0 or j == i-1:
                    b[j] = 1
                else:
                    b[j] = a[j-1]+a[j]    

            a,b = b,a 

        return a
