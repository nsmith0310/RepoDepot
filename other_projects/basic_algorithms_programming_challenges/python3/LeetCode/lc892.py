class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        l = []
        
        i = 0
        while i<len(grid):
            tmp = []
            j = 0
            while j<len(grid[i]):
                num = grid[i][j]
                if num!=0:
                    tmp.append(4*num + 2)
                else:
                    tmp.append(0)
                j+=1
            l.append(tmp)
            i+=1
        
        f = 0
        i = 0
        while i<len(grid):
            j = 0
            while j<len(grid[i]):
                if grid[i][j]!=0:
                    
                    num = l[i][j]
                    if j!=0:
                        if grid[i][j-1]!=0:
                            num-=min([grid[i][j-1],grid[i][j]])
                    if j!=len(grid[i])-1:
                        if grid[i][j+1]!=0:
                            num-=min([grid[i][j+1],grid[i][j]])
                    if i!=0:
                        if grid[i-1][j]!=0:
                            num-=min([grid[i-1][j],grid[i][j]])
                    if i!=len(grid)-1:
                        if grid[i+1][j]!=0:
                            num-=min([grid[i+1][j],grid[i][j]])
                    
                    f+=num
                j+=1
            i+=1
        return f
