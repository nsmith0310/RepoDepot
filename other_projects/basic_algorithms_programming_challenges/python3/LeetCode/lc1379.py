# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        tmp = [cloned]
        
        
        for x in tmp:
            
            if x.val==target.val:
                
                return x
            
            if x.left!=None:
                tmp.append(x.left)
                
            if x.right!=None:
                tmp.append(x.right)
