# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        while queue:
            node, col = queue.popleft()
            ans[col].append(node.val)
            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))
        return [ans[d] for d in sorted(ans)]
