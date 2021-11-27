# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        nums = []

        def inorder(root):
            if root is None:
                return root

            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)

        inorder(root)
        lb = nums.index(low)
        hb = nums.index(high)
        s = 0
        for i in range(lb, hb + 1):
            s += nums[i]
        return s
