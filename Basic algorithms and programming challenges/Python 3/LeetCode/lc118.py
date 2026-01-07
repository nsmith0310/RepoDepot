class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1],[1,1]]
        elif numRows==0:
            return []
        l = [[1],[1,1]]
        i = 2
        while i<numRows:
            tmp = [1]
            j = 0
            while j<len(l[i-1])-1:
                tmp.append(l[i-1][j]+l[i-1][j+1])
                j+=1
            tmp.append(1)
            l.append(tmp)
            i+=1
        return l
