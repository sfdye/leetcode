# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []

        def dfs(root, cur, sum):
            if not root:
                return
            elif not root.left and not root.right and root.val == sum:
                ans.append(cur + [root.val])
            else:
                sum -= root.val
                dfs(root.left, cur + [root.val], sum)
                dfs(root.right, cur + [root.val], sum)

        dfs(root, [], sum)
        return ans
