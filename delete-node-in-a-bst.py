# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def helper(root, key):
            if root is None:
                return None
            if key < root.val:
                root.left = helper(root.left, key)
            elif key > root.val:
                root.right = helper(root.right, key)
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                else:

                    root.val = minval(root.right)

                    root.right = helper(root.right, root.val)
            return root

        def minval(root):

            mn = root.val
            while (root is not None):
                mn = root.val
                root = root.left
            return mn

        return helper(root, key)