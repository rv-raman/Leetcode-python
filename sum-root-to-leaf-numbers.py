# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive(self,root,ans):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            ans=ans*10+root.val
            return ans
        return self.recursive(root.left,ans=ans*10+root.val)+self.recursive(root.right,ans=ans*10+root.val)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans=0
        return self.recursive(root,ans)