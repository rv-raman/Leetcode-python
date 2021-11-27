# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(root, freq):
            if root is None:
                return 0
            freq[root.val] += 1

            if root.left is None and root.right is None:
                nodds = 0
                for i in freq:
                    if i % 2 == 1:
                        nodds += 1
                freq[root.val] -= 1
                if nodds > 1:
                    return 0
                return 1

            ans = dfs(root.left, freq)
            ans += dfs(root.right, freq)
            freq[root.val] -= 1
            return ans

        freq = [0] * 10
        return dfs(root, freq)
