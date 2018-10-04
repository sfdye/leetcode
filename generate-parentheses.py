class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ans = []
        
        def generate(left, right, cur):
            if len(cur) == n*2:
                self.ans.append(cur)
            else:
                if left < n:
                    generate(left+1, right, cur+"(")
                if right < left:
                    generate(left, right+1, cur+")")       
            
        generate(0, 0, "")
        return self.ans
        U