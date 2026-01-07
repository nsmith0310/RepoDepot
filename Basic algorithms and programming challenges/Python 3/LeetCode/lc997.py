class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        l = [0 for i in range(0,N)]
        m = [0 for i in range(0,N)]
        
        count = 0
        for x in trust:
            l[x[0]-1]+=1
            m[x[1]-1]+=1
        
        if 0 in l:
            ind = l.index(0)
            
            if m[ind]==N-1:
                return ind+1
            else:
                return -1
        else:
            return -1
                
