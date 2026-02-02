# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        m = []
        if root!=None:
            
            m+=self.inorderTraversal(root.left)
            m.append(root.val)
            m+=self.inorderTraversal(root.right)
            
        return m
