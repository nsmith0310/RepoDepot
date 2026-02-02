class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:    
        
        f = [0 for i in range(0,len(arr))]
        
        tmp = []
        i = 0
        while i<len(arr):
            tmp.append([arr[i],i])
            i+=1
        tmp.sort(key=lambda x: x[0])
        
        i = 0
        while i<len(tmp)-1:
            if tmp[i][0]==tmp[i+1][0]:
                tmp[i].append(tmp[i+1][1])
                del tmp[i+1]
                i-=1
            i+=1
        i = 0
        while i<len(tmp):
            j = 1
            while j<len(tmp[i]):
                f[tmp[i][j]]=i+1
                j+=1
            i+=1
        return f
        
