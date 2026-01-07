class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = 0
        while n<k:
            
            end = [x[-1] for x in grid]
            tmp = end[-1]
            del end[-1]
            end.insert(0,tmp)
            
            i = 0
            while i<len(grid):
                
                del grid[i][-1]
                grid[i].insert(0,end[i])
                
                i+=1
            n+=1
        return grid
            
            
            
                    
