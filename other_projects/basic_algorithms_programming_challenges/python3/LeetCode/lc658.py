class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = []
        i = 0
        
        while i<len(arr):
            l.append([arr[i],abs(x-arr[i])])
            i+=1
        
        l.sort(key=lambda x: x[1])
        
        f = []
        i = 0
        while i+1<=k:
            f.append(l[i][0])
            i+=1
        f.sort()
        return f
            
