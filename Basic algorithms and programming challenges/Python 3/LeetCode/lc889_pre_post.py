# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recur(self,pre,post):

        if pre!=[]:
            val = pre[0]
            node = TreeNode(val)
            del pre[0]
            if pre!=[]:
                val2 = pre[0]
                i = 0
                while i<len(post):
                    if post[i]==val2:
                        break
                    else:
                        i+=1
                
                node.left = self.recur(pre[:i+1],post[:i+1])
                node.right = self.recur(pre[i+1:],post[i+1:-1])
                    
            return node

           
          
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        return self.recur(pre,post)
