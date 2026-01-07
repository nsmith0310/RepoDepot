class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        mx = 0
        k = 0
        while k<len(grid):
            if len(grid[k])>mx:
                mx = len(grid[k])
            k+=1
            
        tmp = [[] for i in range(0,mx)]
        
        xy = 0
        xz = 0
        yz = 0
        
        i = 0
        while i<len(grid):
            tmp1 = []
            j = 0
            while j<len(grid[i]):
                if grid[i][j]!=0:
                    xy+=1
                tmp1.append(grid[i][j])
                tmp[j].append(grid[i][j])
                j+=1
            xz+=max(tmp1)
            i+=1
        for x in tmp:
            yz+=max(x)
        return xy+xz+yz
