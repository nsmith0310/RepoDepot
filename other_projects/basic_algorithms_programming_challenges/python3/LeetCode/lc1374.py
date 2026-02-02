class Solution:
    def generateTheString(self, n: int) -> str:
        if n<1:
            return ""
        if n&1==True:
            return ''.join(['a' for i in range(1,n+1)])
        else:
            return 'a'+''.join('b' for i in range(1,n))
