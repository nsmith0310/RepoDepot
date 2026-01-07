# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root==None: return 0
        
        
        mx = 1
        tmp = [[root,1]]
        f = []
        
        
        for x in tmp:
            if x[0].right==None and x[0].left==None:
                f.append(x[1]+1)
            if x[0].right!=None:
                tmp.append([x[0].right,x[1]+1])
            if x[0].left!=None:
                tmp.append([x[0].left,x[1]+1])
                
        return min(f)-1
