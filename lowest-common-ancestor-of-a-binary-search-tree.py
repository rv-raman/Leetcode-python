# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < q.val:
            a = p
            b = q
        else:
            a = q
            b = p
        return self.helper(root, a, b)

    def helper(self, root, a, b):
        if a.val <= root.val and b.val >= root.val:
            return root
        if a.val > root.val:
            return self.helper(root.right, a, b)
        if a.val < root.val:
            return self.helper(root.left, a, b)

#         if root is None:
#             return None
#         if root == p or root == q:
#             return root
#         left = self.lowestCommonAncestor(root.left,p,q)
#         right = self.lowestCommonAncestor(root.right,p,q)
#         if left and right:
#             return root
#         if left:
#             return left
#         if right:
#             return right
#         return None
