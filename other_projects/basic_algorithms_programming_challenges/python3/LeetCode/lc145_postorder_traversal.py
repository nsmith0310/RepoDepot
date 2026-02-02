# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        m = []
        if root!=None:
            
            m+=self.postorderTraversal(root.left)
            m+=self.postorderTraversal(root.right)
            m.append(root.val)
        return m
