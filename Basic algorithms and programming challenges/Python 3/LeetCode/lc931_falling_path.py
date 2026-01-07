###same basic idea as descending pyramid

class Solution:
    
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        
        
        lim = len(A)
        for i in range(lim-1,0,-1):
            for j in range(lim):
                A[i-1][j]+=min(A[i][max(0,j-1):min(lim,j+2)])
                
        return min(A[0])
            
            
