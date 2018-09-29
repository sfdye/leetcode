# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        pre, cur, stack, cur_count, max_count, modes = None, root, [], 0, 0, []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if not pre or cur.val == pre.val:
                cur_count += 1
            else:
                if cur_count > max_count:
                    max_count = cur_count
                    modes = [pre.val]
                elif cur_count == max_count:
                    modes.append(pre.val)
                cur_count = 1
            pre = cur
            cur = cur.right
        if cur_count > max_count:
            return [pre.val]
        elif cur_count == max_count:
            modes.append(pre.val)
        return modes

