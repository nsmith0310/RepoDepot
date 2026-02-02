# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.m=[]
        if root!=None:
            self.l = []
            tmp = [root]
            for x in tmp:
                self.l.append(x.val)
                if x.left!=None:
                    tmp.append(x.left)
                if x.right!=None:
                    tmp.append(x.right)
            self.m = list(set(self.l))
            self.m.sort()
        self.lim = len(self.m)  

    def next(self) -> int:
        """
        @return the next smallest number
        """
        val = self.m[0]
        del self.m[0]
        self.lim-=1
        return val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.lim >0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
