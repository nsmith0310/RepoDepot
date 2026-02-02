# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        
        if root==None: return ""
        f = []
        
        tmp = [[root,""]]
        
        
        for x in tmp:
            if x[0].left==None and x[0].right==None:
                f.append((x[1]+chr(x[0].val+97))[::-1])
            if x[0].left!=None:
                tmp.append([x[0].left,x[1]+chr(x[0].val+97)])
            if x[0].right!=None:
                tmp.append([x[0].right,x[1]+chr(x[0].val+97)])
        f.sort()
        
        return f[0]
                
                
        
