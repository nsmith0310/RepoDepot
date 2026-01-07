class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if len(matrix[0])==1:
            return True
        
    
        i = 0
        while i<len(matrix)-1:
            j = 0
            while j<len(matrix[i])-1:
                if matrix[i+1][j+1]!=matrix[i][j]:return False
                j+=1
            i+=1
        return True
