class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.n = matrix
        self.val=[]
        self.s = []
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        t = 0
        try:
            return self.s[self.val.index([row1,col1,row2,col2])]
        except:
            pass
        for i in range(row1,row2+1):
            for j in range(col1,col2+1):
                t+=self.n[i][j]
                
        self.val.append([row1,col1,row2,col2])
        self.s.append(t)
        return t
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
