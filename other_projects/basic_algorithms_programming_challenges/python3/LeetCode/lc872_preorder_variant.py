# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def preo(self, node):
        m = []
        if node!=None:
            if node.left==None and node.right==None:
                m.append(node.val)
            m+=self.preo(node.left)
            m+=self.preo(node.right)
        return m
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        a = self.preo(root1)
        b = self.preo(root2)
        
        return a==b
