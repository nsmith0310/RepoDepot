# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        if t1!=None or t2!=None:
            
            if t1!=None and t2!=None:
                node = TreeNode(t1.val + t2.val)
                node.left = self.mergeTrees(t1.left,t2.left)
                node.right = self.mergeTrees(t1.right,t2.right)
            elif t1!=None:
                node = TreeNode(t1.val)
                node.left = self.mergeTrees(t1.left,t2)
                node.right = self.mergeTrees(t1.right,t2)
                
            else:
                node = TreeNode(t2.val)
                node.left = self.mergeTrees(t1,t2.left)
                node.right = self.mergeTrees(t1,t2.right)
            
            
            return node
