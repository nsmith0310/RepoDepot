class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        c=0
        
        i = 0
        while i<len(arr1):
            t = 0
            j = 0
            while j<len(arr2):
                if abs(arr1[i]-arr2[j])<=d:
                    
                    t = 1
                    break
                j+=1
            if t==0 and j==len(arr2):
                c+=1
            i+=1
        return c
            
