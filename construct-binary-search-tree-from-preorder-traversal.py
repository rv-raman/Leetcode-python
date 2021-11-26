# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)

        def bstFromPreorderandInorder(preorder, inorder):
            if len(preorder) == 0 or len(inorder) == 0:
                return None
            root = TreeNode(preorder[0])
            root.left = bstFromPreorderandInorder(preorder[1:inorder.index(root.val) + 1],
                                                  inorder[:inorder.index(root.val)])
            root.right = bstFromPreorderandInorder(preorder[inorder.index(root.val) + 1:],
                                                   inorder[inorder.index(root.val) + 1:])
            return root

        #         def treeConstruct(ist,ie,p):
        #             if ist>ie:
        #                 return None

        #             node = TreeNode(preorder[p])
        #             p+=1
        #             if ist==ie:
        #                 return node
        #             idx = inorder.index(node.val)
        #             node.left = treeConstruct(ist,idx-1,p)
        #             node.right = treeConstruct(idx+1,ie,p)

        #             return node
        return bstFromPreorderandInorder(preorder, inorder)

