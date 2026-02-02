# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root==None:return 0
        
        l = []
        tmp = [[root,str(root.val)]]
        
        for x in tmp:
            if x[0].left == None and x[0].right==None:
                l.append(x[1]+str(x[0].val))
                
            if x[0].left!=None:
                tmp.append([x[0].left,x[1]+str(x[0].val)])
            if x[0].right!=None:
                tmp.append([x[0].right,x[1]+str(x[0].val)])
            
        s = 0
        print(l)
        for x in l:
            s+=int(x[1:],2)
        return s
