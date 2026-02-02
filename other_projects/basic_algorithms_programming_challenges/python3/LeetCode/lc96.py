from math import factorial as f
class Solution:
    
    def b(self,n):
        return (f(2*n)//(f(n)*f(n+1)))
        
    def numTrees(self, n: int) -> int:
        return self.b(n)
