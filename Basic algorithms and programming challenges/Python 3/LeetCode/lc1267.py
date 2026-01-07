class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        r = [[] for x in grid]
        c = [[] for x in grid[0]]
        
        i = 0
        while i<len(grid):
            j = 0
            while j<len(grid[i]):
                if grid[i][j]==1:
                    r[i].append(str(i)+"."+str(j))
                    c[j].append(str(i)+"."+str(j))
                j+=1
            i+=1
            
        
        
        l = set()
        
        total = 0
        
        i = 0
        while i<len(r):
            if len(r[i])>1:
                for x in r[i]:
                    l.add(x)
            
                   
            i+=1
            
        i = 0
        while i<len(c):
            if len(c[i])>1:
                for x in c[i]:
                    l.add(x)            
            i+=1
        
        
        
        return len(list(l))
                
