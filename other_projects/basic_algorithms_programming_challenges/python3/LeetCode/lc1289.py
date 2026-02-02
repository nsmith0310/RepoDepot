class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        
        lim = len(arr)
        for i in range(lim-1,0,-1):
            for j in range(lim):
                arr[i-1][j]+=min(arr[i][0:j] +arr[i][j+1:lim])
        
        
        return min(arr[0])
