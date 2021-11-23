"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        from collections import deque
        ans = []
        if root == None:
            return ans
        q = deque()
        q.append(root)
        while q:
            temp = []
            n = len(q)
            for i in range(n):
                node = q.popleft()
                temp.append(node.val)
                for i in node.children:
                    q.append(i)
            ans.append(temp)
        return ans

