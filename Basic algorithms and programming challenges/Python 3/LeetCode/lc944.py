class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        
        B = [list(x) for x in A]
        lim = len(B)
        if lim<=1:return 0
        c=0
        j = 0
        while j<len(B[0]):
            i = 0
            while i<len(B)-1:
                if ord(B[i][j])>ord(B[i+1][j]):
                    c+=1
                    break
                i+=1
            j+=1
        
        
        return c
                
            
            
