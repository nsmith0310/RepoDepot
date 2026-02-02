class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        c = 0
        
        i = 0
        
        
        
        
        s = sum(arr[i:i+k])
        if s/k>=threshold:c+=1
            
        while i<len(arr)-k:
            s-=arr[i]
            
            s+=arr[i+k]
            if s/k>=threshold:c+=1
            i+=1
        return c
