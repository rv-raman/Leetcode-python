"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        from collections import deque
        ans = []
        if root is None:
            return root
        ans1 = root
        q = deque()
        q.append(root)
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                ans.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(None)
        print(ans)

        i = 0
        n = len(ans)
        while i < n:
            if ans[i] is None:
                i += 1
                continue
            else:
                ans[i].next = ans[i + 1]
                i += 1
        return ans1






