class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        l = [[0 for i in range(0,len(M[0]))] for j in range(0,len(M))]
        
        i = 0
        while i<len(M):
            j = 0
            while j<len(M[i]):
                tmp = [M[i][j]]

                if i>0:
                    tmp.append(M[i-1][j])
                        
                if i<len(M)-1:
                    tmp.append(M[i+1][j])
                        
                if j>0:
                    tmp.append(M[i][j-1])
                        
                if j<len(M[i])-1:
                    tmp.append(M[i][j+1])
                        
                if i>0 and j>0:
                    tmp.append(M[i-1][j-1])
                        
                if i>0 and j<len(M[i])-1:
                    tmp.append(M[i-1][j+1])
                       
                if i<len(M)-1 and j>0:
                    tmp.append(M[i+1][j-1])
                        
                if i<len(M)-1 and j<len(M[i])-1:
                    tmp.append(M[i+1][j+1])
                        
                l[i][j]=sum(tmp)//len(tmp)
                
                j+=1
            i+=1
        return l
