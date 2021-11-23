# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findPath(self, root, node, ans):
        if root is None:
            return False
        ans.append(root)
        if root.val == node.val:
            return True
        if self.findPath(root.left, node, ans) or self.findPath(root.right, node, ans):
            return True
        ans.pop()
        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val or root.val == q.val:
            return root
        if not root.left and not root.right:
            return None
        lft = rht = None
        if root.left:
            lft = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            rht = self.lowestCommonAncestor(root.right, p, q)
        if lft and rht:
            return root
        if not lft:
            return rht
        return lft
        # path1=[]
        # path2=[]
        # self.findPath(root,p,path1)
        # self.findPath(root,q,path2)
        # finalans=-1
        # i=j=0
        # while i<len(path1) and j<len(path2):
        #     if path1[i].val==path2[j].val:
        #         finalans = path1[i]
        #     i+=1
        #     j+=1
        # return finalans

