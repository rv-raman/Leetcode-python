# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, root1):
        if root == None and root1 == None:
            return True
        if root == None or root1 == None:
            return False
        if root.val != root1.val:
            return False
        return self.helper(root.left, root1.right) and self.helper(root.right, root1.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, root)
