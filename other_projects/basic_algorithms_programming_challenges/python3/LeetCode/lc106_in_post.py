# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def recur(self,inorder,post):
        ###print(inorder,post)
        
        if post!=[]:
            val =post[-1]
            del post[-1]
            node = TreeNode(val)
            i = 0
            while i<len(inorder):
                if inorder[i]==val:
                    break
                else:
                    i+=1
            
            node.left = self.recur(inorder[:i],post[:i])
            node.right = self.recur(inorder[i+1:],post[i:])
            return node
       
            
    
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        return self.recur(inorder,postorder)
