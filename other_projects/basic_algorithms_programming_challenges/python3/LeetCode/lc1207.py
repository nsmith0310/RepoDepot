class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        l = []
        i = 0
        t=[]
        while i<len(arr):
            if arr[i] not in t:
                l.append(arr.count(arr[i]))
                t.append(arr[i])
            i+=1
            
        
            
        
        return len(list(set(l)))==len(l)
