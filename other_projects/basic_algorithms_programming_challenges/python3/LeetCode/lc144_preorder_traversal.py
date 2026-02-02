# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
                                            
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        m = []
        if root!=None:
            m.append(root.val)
            m+=self.preorderTraversal(root.left)
            m+=self.preorderTraversal(root.right)
        return m
            
                
            
            
        
        
