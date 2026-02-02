# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root==None: return root
        
        l = [root]
        tmp = [root]
        
        while 1!=-1:
            t = 0
            for x in tmp:
            
                if x.left!=None:
                    if x.left.left==None and x.left.right==None:
                        if x.left.val == target:
                            x.left=None
                            t = 1
                    else:
                        tmp.append(x.left)
                if x.right!=None:
                    if x.right.left==None and x.right.right==None:
                        if x.right.val == target:
                            x.right=None
                            t = 1
                    else:
                        tmp.append(x.right)
                
            if t==0:
                break
            
        if tmp[0].val == target and tmp[0].left==None and tmp[0].right==None:
            return None
        return tmp[0]
