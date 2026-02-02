class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 or n==1: return 1
        
        l = [m,n]
        l.sort()
        
        ###start with values for 2
        tmp = [i for i in range(1,l[1]+1)]
        tmp2 = [1]
        
        j = 2
        while j<l[0]:
            
            i = 1
            while i<len(tmp):
                tmp2.append(tmp2[-1]+tmp[i])
                i+=1
            tmp = tmp2
            tmp2 = [1]
            j+=1
        return tmp[-1]
        
