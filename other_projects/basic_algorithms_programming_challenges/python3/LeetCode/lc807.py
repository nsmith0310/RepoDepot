class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        start = 0
        line = []
        tmp = []
        for x in grid:
            tmp.append(max(x))
            start+=sum(x)
        line.append(tmp)
        
        tmp = [[] for x in grid]
        
        i = 0
        while i<len(grid):
            j = 0
            while j<len(grid):
                tmp[j].append(grid[i][j])
                j+=1
            i+=1
        tmp2 = []
        for x in tmp:
            tmp2.append(max(x))
        line.append(tmp2)
        
        mx = 0
        
        i = 0
        while i<len(grid):
            j = 0
            while j<len(grid):
                grid[i][j]=min([line[0][i],line[1][j]])
                j+=1
            i+=1
        
        for x in grid:
            
            mx+=sum(x)
        return mx-start
                
                
