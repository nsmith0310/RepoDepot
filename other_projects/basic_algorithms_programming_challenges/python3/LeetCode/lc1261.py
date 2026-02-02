# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        self.arr = set()
        root.val = 0
        tmp = [root]
        for x in tmp:
            self.arr.add(x.val)
            if x.left!=None:
                x.left.val = 2*x.val + 1
                self.arr.add(x.left.val)
                tmp.append(x.left)
            if x.right!=None:
                x.right.val = 2*x.val + 2
                self.arr.add(x.right.val)
                tmp.append(x.right)
        
    def find(self, target: int) -> bool:
        return target in self.arr


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
