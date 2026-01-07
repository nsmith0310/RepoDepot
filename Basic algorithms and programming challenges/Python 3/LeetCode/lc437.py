# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root==None: return 0
        
        c = 0
        
        tmp = [root]
        
        for x in tmp:
            if x.left!=None:
                tmp.append(x.left)
            if x.right!=None:
                tmp.append(x.right)
                
                
        for x in tmp:
            tmp2 = [[x,x.val]]
            if x.val==sum: c+=1
            for y in tmp2:
                if y[0].left!=None:
                    val = y[1]+y[0].left.val
                    if val==sum: c+=1
                    tmp2.append([y[0].left,val])
                
                if y[0].right!=None:
                    val = y[1]+y[0].right.val
                    if val==sum: c+=1
                    tmp2.append([y[0].right,val])
        return c
                    
        
