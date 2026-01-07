class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        
        
        while 1!=-1:
            t = 0
            i = 0
            while i<len(M):
                j = 0
                while j<len(M):
                    if M[i][j]==1 and j!=i:
                        a = 0
                        while a<len(M):
                            if M[j][a]==0 and M[i][a]==1:
                                M[j][a]=1
                                t=1
                            a+=1
                    j+=1
                i+=1
            if t==0:
                break
        
        z = set()
        for x in M:
            st = ''.join(list(map(str,x)))
            
            z.add(st)
            
        return len(list(z))
