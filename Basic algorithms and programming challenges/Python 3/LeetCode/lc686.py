class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        
        tmp = A
        if len(A)>len(B):        
            l = len(A)//len(B)
        else:
            l = len(B)//len(A)
            
        c=0
        while c<=2*l:
            if B in tmp:
                return c+1
            c+=1
            tmp+=A
        return -1
