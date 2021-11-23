# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        ans = []
        q = deque()
        if root == None:
            return ans
        q.append(root)
        while q:
            temp = []
            n = len(q)
            for i in range(n):
                tNode = q.popleft()
                temp.append(tNode.val)
                if tNode.left != None:
                    q.append(tNode.left)
                if tNode.right != None:
                    q.append(tNode.right)
            ans.append(temp)
        return ans
