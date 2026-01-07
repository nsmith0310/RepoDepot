# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root==None: return root

       

        

        l = []

       

        tmp = [root]

       

        tmp

        for x in tmp:

            if x.left!=None:
                tmp.append(x.left)

            if x.right!=None:
                tmp.append(x.right)

                 
        tmp = tmp[::-1]
        for x in tmp:
            tmp2 = [x]
            a = 0
            b = 0
            if tmp2[0].val==p.val:
                a = 1
            if tmp2[0].val==q.val:
                b = 1
                
            for y in tmp2:
                if y.val==p.val:
                    a = 1
                elif y.val==q.val:
                    b = 1

                if y.right!=None:
                    tmp2.append(y.right)
                if y.left!=None:
                    tmp2.append(y.left)

            if a==1 and b==1:
                return tmp2[0]
