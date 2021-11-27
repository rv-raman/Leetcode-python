# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    s = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        def func(root):
            if root is None:
                return
            func(root.right)
            Solution.s += root.val
            root.val = Solution.s
            func(root.left)

        Solution.s = 0
        func(root)
        return root
#         nums=[]
#         roots=[]
#         def inorder(root):
#             if root is None:
#                 return root
#             inorder(root.left)
#             nums.append(root.val)
#             roots.append(root)
#             inorder(root.right)
#         inorder(root)
#         dt={}
#         n=len(nums)-1
#         dt[nums[n]]=0
#         for i in range(n-1,-1,-1):
#             dt[nums[i]]=dt[nums[i+1]]+nums[i+1]

#         print("dt is ",dt)
#         for i in range(n+1):
#             roots[i].val=roots[i].val+dt[roots[i].val]

#         return root