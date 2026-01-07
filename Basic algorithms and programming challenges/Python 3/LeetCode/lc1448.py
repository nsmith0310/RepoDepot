# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root==None:
            return 0
        
        tmp = [[root,root.val]]
        
        for x in tmp:
            if x[0].left!=None:
                tmp.append([x[0].left,max(x[1],x[0].left.val)])
            if x[0].right!=None:
                tmp.append([x[0].right,max(x[1],x[0].right.val)])
        c = 0       
        for x in tmp:
            if x[0].val>=x[1]:c+=1
        return c
