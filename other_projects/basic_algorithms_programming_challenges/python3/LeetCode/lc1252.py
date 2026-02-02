class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        arr=[]
        i = 1
        while i<=n:
            arr.append([0 for j in range(0,m)])
            i+=1
        for x in indices:
            r = x[0]
            c = x[1]
            
            
            j = 0
            while j<n:
                arr[j][c]+=1
                j+=1
            j = 0
            while j<m:
                arr[r][j]+=1
                j+=1
            
        c=0
        for x in arr:
            for y in x:
                if y&1==True:
                    c+=1
        return c
                
