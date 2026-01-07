# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        
        if root!=None:
            
            if root.val<L or root.val>R:
                val = self.trimBST(root.left,L,R)
                if val==None:
                    root = self.trimBST(root.right,L,R)
                else:
                    root = val
            else:
                root.left = self.trimBST(root.left,L,R)
                root.right = self.trimBST(root.right,L,R)
        return root
            
        
