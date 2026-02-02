# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:    
    def pre(self,S):
        
        if S!="":
            tmp = ""
            i=0
            
            while i<len(S):
                if S[i]=="-":
                    break
                else:
                    tmp+=S[i]
                i+=1
            
            node = TreeNode(int(tmp))
            ls = i
            rs = len(S)+1
            count = 0
            while i<len(S) and S[i]=="-":
                count+=1
                i+=1
                
            c = 0
            while i<len(S):
                if S[i]=="-":
                    c+=1
                else:
                    
                    if c==count:
                        rs = i
                        break
                    c=0
                i+=1
            
            node.left = self.pre(S[ls+count:rs])
            node.right = self.pre(S[rs:])
            return node
                
                
                
            
            
            
        
            
    def recoverFromPreorder(self, S: str) -> TreeNode:
        
        return self.pre(S)
