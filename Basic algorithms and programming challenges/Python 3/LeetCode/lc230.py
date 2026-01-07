# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        l = []
        
        tmp = [root]
        for x in tmp:
            l.append(x.val)
            if x.left!=None:
                tmp.append(x.left)
            if x.right!=None:
                tmp.append(x.right)
        l.sort()
        
        return l[k-1]
