# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root==None: return root
        
        
        tmp = [root]
        
        for x in tmp:
            if x.val==val: return x
            
            if x.left!=None:
                tmp.append(x.left)
            if x.right!=None:
                tmp.append(x.right)
        return None
        
        
