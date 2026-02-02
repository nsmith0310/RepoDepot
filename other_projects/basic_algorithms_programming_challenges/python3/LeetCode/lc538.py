# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        
        if root==None: return root
        l = []
        
        tmp = [root]
        
        for x in tmp:
            l.append(x.val)
            if x.right!=None:
                tmp.append(x.right)
            if x.left!=None:
                tmp.append(x.left)
                
        l.sort()
        
        tmp2 = [root]
        
        for y in tmp2:
            if y!=None:
                
                y.val+=sum(l[l.index(y.val)+1:])
            if y.right!=None:
                tmp2.append(y.right)
            if y.left!=None:
                tmp2.append(y.left)
        
        return tmp2[0]
