# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        from collections import deque
        q = deque()
        q.append(root)
        parents = [-1] * 101
        levels = [-1] * 101
        level = 0
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    parents[node.left.val] = node.val
                    levels[node.left.val] = level
                if node.right:
                    q.append(node.right)
                    parents[node.right.val] = node.val
                    levels[node.right.val] = level
            level += 1

        if parents[x] != parents[y] and levels[x] == levels[y]:
            return True
        return False


