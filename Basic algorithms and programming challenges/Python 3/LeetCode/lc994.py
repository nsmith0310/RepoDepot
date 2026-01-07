from copy import deepcopy
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        tmp = deepcopy(grid)
        
        
        
        
        c = 0
        
        while 1!=-1:
            t = 0
            i = 0
            while i<len(grid):
                j = 0
                while j<len(grid[i]):
                    if grid[i][j]==2:
                        if i>0:
                            if grid[i-1][j]==1:
                                tmp[i-1][j]=2
                                
                                t=1
                        if i<len(grid)-1:
                            if grid[i+1][j]==1:
                                tmp[i+1][j]=2
                                
                                t=1
                        if j>0:
                            if grid[i][j-1]==1:
                                tmp[i][j-1]=2
                                t=1
                        if j<len(grid[i])-1:
                            if grid[i][j+1]==1:
                                tmp[i][j+1]=2
                                t=1
                    j+=1
                i+=1
            grid = deepcopy(tmp)
            
            
            if t==0:
                break
            c+=1
        for x in grid:
            if 1 in x:
                return -1
            
        return c
                        
