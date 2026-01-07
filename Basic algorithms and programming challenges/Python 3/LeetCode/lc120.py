class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        
        if len(triangle)==1:
            return triangle[0][0]

        i = 1
        while i<len(triangle):
            j = 0
            while j<len(triangle[i]):
                if j!=0 and j!=len(triangle[i])-1:
                    
                    
                    if triangle[i][j]+triangle[i-1][j]<triangle[i][j]+triangle[i-1][j-1]:
                        triangle[i][j]+=triangle[i-1][j]
                    else:
                        triangle[i][j]+=triangle[i-1][j-1]
                elif j==0:
                    triangle[i][j]+=triangle[i-1][j]
                else:
                    triangle[i][j]+=triangle[i-1][-1]
                j+=1
            i+=1
            
        
        
        return(min(triangle[-1]))
