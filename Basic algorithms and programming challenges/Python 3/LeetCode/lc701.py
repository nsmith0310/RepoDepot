# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if root==None: return TreeNode(val)
        
        tmp = [root]
        c = 0
        for x in tmp:
            if x!=None:
                
                if val<x.val and x.left==None:
                    x.left=TreeNode(val)
                        
                    break
                
                elif val>x.val and x.right==None:
                    x.right=TreeNode(val)
                        
                    break
                if val<x.val:
                    tmp.append(x.left)
                elif val>x.val:
                    tmp.append(x.right)
        
        return tmp[0]
            
