# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root==None: return root
        
        tmp = [root]
        l = []
        for x in tmp:
            if x.val!=None:
                l.append(x.val)
            if x.right!=None:
                tmp.append(x.right)
            if x.left!=None:
                tmp.append(x.left)
                
        l.sort()
        l2 = [TreeNode(x) for x in l]
        if len(l2)==1:
            return l2[0]
        i = len(l2)-1
        while i>=1:
            l2[i-1].right = l2[i]
            i-=1
        return l2[0]
            
        
