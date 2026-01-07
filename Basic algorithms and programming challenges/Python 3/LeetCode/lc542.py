class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        row = len(matrix)
        col = len(matrix[0])
        
        
        while 1==1:
            t = 0
            i = 0
        
            while i<row:
                j = 0
                while j<col:
                
                    if matrix[i][j]!=0:
                        tmp = []
                    
                        if i>0:
                            tmp.append(matrix[i-1][j])
                    
                    
                        if i<row-1:
                            tmp.append(matrix[i+1][j])
                    
                        if j>0:
                            tmp.append(matrix[i][j-1])
                    
                    
                        if j<col-1:
                            tmp.append(matrix[i][j+1])
                        
                        
                        num = min(tmp)+1
                        if matrix[i][j]!=num:
                            matrix[i][j]=num
                            t = 1
                    j+=1
                i+=1
            if t==0:
                break
        return matrix
