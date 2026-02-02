class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        lim1 = len(matrix)
        lim2 = len(matrix[0])
        
        t = sum([sum(x) for x in matrix])
            
        s = 2
        
        end = min([lim1,lim2])
        
        while s<=end:    
            i = 0
            while i+s<=lim1:
            
                j = 0
                while j+s<=lim2:
                    if matrix[i][j]==1 and matrix[i][j+s-1]==1 and matrix[i+s-1][j]==1 and matrix[i+s-1][j+s-1]==1:
                        a = i
                        while a<i+s:
                            f = 0
                        
                            b = j
                            while b<j+s:
                                if matrix[a][b]==0:
                                    f=1
                                    break
                            
                                b+=1
                            if f ==1:
                                break
                            a+=1
                    
                        if f==0:
                            t+=1
                    
                    j+=1
                i+=1
            s+=1
            
        return t
