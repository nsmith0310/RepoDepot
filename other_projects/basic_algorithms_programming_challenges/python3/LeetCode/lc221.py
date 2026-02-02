class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix==[] or matrix==[[]]: return 0
        lim1 = len(matrix)
        lim2 = len(matrix[0])
        
        
            
        s = min([lim1,lim2])
        
        end = 2
        
        while s>=end:    
            i = 0
            while i+s<=lim1:
            
                j = 0
                while j+s<=lim2:
                    
                    a = i
                    while a<i+s:
                        f = 0
                        
                        b = j
                        while b<j+s:
                            if matrix[a][b]=='0':
                                f=1
                                break
                            
                            b+=1
                        if f ==1:
                            break
                        a+=1
                    
                    if f==0:
                        return s**2
                    
                    j+=1
                i+=1
            s-=1
        for x in matrix:
            if '1' in x:return 1
        return 0
