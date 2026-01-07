class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        f = []
        
        
        i = 0
        while i<R:
            j = 0
            while j<C:
                f.append([i,j,abs(r0-i)+abs(c0-j)])
                j+=1
            i+=1
        f.sort(key=lambda x: x[2])
        
        final = []
        for x in f:
            final.append([x[0],x[1]])
        return final
