# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums):
        if nums!=[]:
            num = max(nums)
            ind = nums.index(num)
            L = nums[:ind]
            R = nums[ind+1:]

            num = TreeNode(num)

            num.right = self.constructMaximumBinaryTree(R)
            num.left = self.constructMaximumBinaryTree(L)

            return num
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        m = []
        if root!=None:
            
            m+=self.inorderTraversal(root.left)
            m.append(root.val)
            m+=self.inorderTraversal(root.right)
            
        return m
                
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        l = self.inorderTraversal(root)
        l.append(val)
        return self.constructMaximumBinaryTree(l)
        
                
        
        
        
