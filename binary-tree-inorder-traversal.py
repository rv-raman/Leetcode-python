# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def helper(self,root,ans):
    #     if root==None:
    #         return
    #     self.helper(root.left,ans)
    #     ans.append(root.val)
    #     self.helper(root.right,ans)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        st = []
        while root != None:
            ans.append(root.val)
            if root.right != None:
                st.append(root.right)
            root = root.left
            if root == None and len(st) != 0:
                root = st.pop()
            return ans
#         ans=[]
#         self.helper(root,ans)
#         return ans
