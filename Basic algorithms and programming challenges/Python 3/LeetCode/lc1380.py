class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        f = []
        i = 0
        while i<len(matrix):
            j = 0
            while j<len(matrix[i]):
                if min(matrix[i])==matrix[i][j]:
                    mx = 0
                    k = 0
                    while k<len(matrix):
                        if matrix[k][j]>mx:
                            mx = matrix[k][j]
                        k+=1
                    if mx == matrix[i][j]:
                        f.append(matrix[i][j])
                j+=1
            i+=1
        return f
