class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        l = len(arr)
        
        p = [x for x in arr]
        p.sort()
        
        mn = min(arr)
        c = 0
        i = 0
        
        
        while 1!=-1:
            t = 0
            i = 0
            while i<len(arr):
                tmp2= arr[:i+1]
                tmp2.sort()
                if tmp2==p[:i+1]:
                    c+=1
                    del arr[:i+1]
                    del p[:i+1]
                    t = 1
                    i=0
                else:
                    i+=1
            if t==0:
                return c
                
                    
        
