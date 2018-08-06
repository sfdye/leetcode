class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        self.nums = []

        def inorder(node):
            if node:
                inorder(node.left)
                self.nums.append(node.val)
                inorder(node.right)

        inorder(root)
        l, r = 0, len(self.nums)-1
        while l < r:
            if self.nums[l] + self.nums[r] == k:
                return True
            if self.nums[l] + self.nums[r] < k:
                l += 1
            else:
                r -= 1
        return False
