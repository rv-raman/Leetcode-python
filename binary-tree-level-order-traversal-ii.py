# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
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
                node = q.popleft()
                temp.append(node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            ans.append(temp)
        return ans[::-1]



