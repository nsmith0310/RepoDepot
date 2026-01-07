class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        l = []
        
        
        i = 0
        while i<len(grid):
            tmp = []
            j = 0
            while j<len(grid[i]):
                if grid[i][j]==1:
                    tmp.append(4)
                else:
                    tmp.append(0)
                j+=1
            l.append(tmp)
            i+=1
            
        i = 0
        while i<len(grid):
            j = 0
            while j<len(grid[i]):
                if grid[i][j]==1:
                    if i>0:
                        if grid[i-1][j]==1:
                            l[i][j]-=1
                    if i<len(grid)-1:
                        if grid[i+1][j]==1:
                            l[i][j]-=1
                    if j>0:
                        if grid[i][j-1]==1:
                            l[i][j]-=1
                    if j<len(grid[i])-1:
                        if grid[i][j+1]==1:
                            l[i][j]-=1
                j+=1
            i+=1
        t = 0
        for x in l:
            t+=sum(x)
        return t
        
