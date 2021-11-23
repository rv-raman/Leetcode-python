"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def recursive(self, root, ans):
        if root != None:
            for i in root.children:
                self.recursive(i, ans)
            ans.append(root.val)

    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        self.recursive(root, ans)
        return ans
