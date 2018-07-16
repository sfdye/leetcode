# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, depth):

        if root == None:
            return
        else:
            if len(ans) <= depth:
                ans.append([root.val])
            else:
                ans[depth].append(root.val)

            self.dfs(root.left, depth+1)
            self.dfs(root.right, depth+1)
            
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        global ans

        ans = []

        self.dfs(root, 0)

        return ans[::-1]
        
