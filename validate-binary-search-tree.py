# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, mn, mx):
        if root is None:
            return True

        return mn < root.val and root.val < mx and self.helper(root.left, mn, root.val) and self.helper(root.right,
                                                                                                        root.val, mx)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        mn = -1 * (2 ** 31) - 1
        mx = 2 ** 31
        return self.helper(root, mn, mx)
