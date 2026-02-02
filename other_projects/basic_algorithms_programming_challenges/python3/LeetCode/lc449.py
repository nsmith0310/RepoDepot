# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def bstFromPreorder(self, preorder):
        if preorder!=[]:
            node = TreeNode(preorder[0])
            i = 1
            while i<len(preorder) and preorder[i]<preorder[0]:
                i+=1
            node.left = self.bstFromPreorder(preorder[1:i])
            node.right = self.bstFromPreorder(preorder[i:])

            return node
    def preorder(self,tree):
        m = []
        
        if tree!=None:
            m.append(tree.val)
            m+=self.preorder(tree.left)
            m+=self.preorder(tree.right)
        return m
    
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        
        k = '*'.join(list(map(str,self.preorder(root))))
        return k
        
        
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        
        if data!='':
            l = list(map(int,data.split("*")))
            return self.bstFromPreorder(l)
        else:
            return None

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
