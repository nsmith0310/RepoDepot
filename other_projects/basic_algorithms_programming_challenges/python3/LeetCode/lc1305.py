# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        
        
        l = []
        
        if root1!=None:
            tmp = [root1]
            for x in tmp:
                l.append(x.val)
                if x.right!=None:
                    tmp.append(x.right)
                if x.left!=None:
                    tmp.append(x.left)
                    
        if root2!=None:
            tmp = [root2]
            for y in tmp:
                l.append(y.val)
                if y.right!=None:
                    tmp.append(y.right)
                if y.left!=None:
                    tmp.append(y.left)
        l.sort()
        return l
