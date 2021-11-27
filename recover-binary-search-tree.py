# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nums = []

        # print("type of root",type(root))
        def inorder(root):
            if root is None:
                return None

            inorder(root.left)
            nums.append(root)
            inorder(root.right)

        inorder(root)
        snums = sorted(nums, key=lambda x: x.val)
        n = len(nums)
        for i in range(n):
            if nums[i].val != snums[i].val:
                nums[i].val, snums[i].val = snums[i].val, nums[i].val
                break

        return root

