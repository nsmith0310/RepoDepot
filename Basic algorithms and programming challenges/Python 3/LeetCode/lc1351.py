class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0
        for x in grid:
            for y in x:
                if y<0:
                    c+=1
        return c
