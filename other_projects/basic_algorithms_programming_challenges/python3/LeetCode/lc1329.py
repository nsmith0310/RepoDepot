class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        new = [[0 for y in mat[0]] for x in mat]
        
        rlim = len(mat)
        clim = len(mat[0])
        
        if rlim-1<2:return mat
        if clim-1<2:return mat
        l1 = []
        l2 = []
        
        if rlim>clim:
            m = rlim
        else:
            m=clim
        c = 0
        while c<clim:
            tmp = [[0,c]]
            
            i = c
            while i<m:
                
                tmp.append([tmp[-1][0]+1,tmp[-1][1]+1])
                i+=1
            i = 0
            while i<len(tmp):
                if tmp[i][0]>=rlim or tmp[i][1]>=clim:
                    del tmp[i]
                    i-=1
                i+=1
            l1.append(tmp)
            tmp2 = []
            for x in tmp:
                tmp2.append(mat[x[0]][x[1]])
            tmp2.sort()
            l2.append(tmp2)
            c+=1
        
        
        
        l3 = []
        l4 = []
        
        
        c = 1
        while c<rlim:
            tmp = [[c,0]]
            i = c
            while i<m:
                
                tmp.append([tmp[-1][0]+1,tmp[-1][1]+1])
                i+=1
            i = 0
            while i<len(tmp):
                if tmp[i][0]>=rlim or tmp[i][1]>=clim:
                    del tmp[i]
                    i-=1
                i+=1
            l3.append(tmp)
            tmp2 = []
            for x in tmp:
                tmp2.append(mat[x[0]][x[1]])
            tmp2.sort()
            l4.append(tmp2)
            c+=1
        
        
        i = 0
        while i<len(l1):
            j = 0
            while j<len(l1[i]):
                new[l1[i][j][0]][l1[i][j][1]]=l2[i][j]
                j+=1
            i+=1
        i = 0
        while i<len(l3):
            j = 0
            while j<len(l3[i]):
                new[l3[i][j][0]][l3[i][j][1]]=l4[i][j]
                j+=1
            i+=1
            
        
        return new
