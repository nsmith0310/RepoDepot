class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        lim = len(timeSeries)
        if lim==1:
            return duration
        if duration==0 or timeSeries==[]:return 0
        
        
        t = 0
        
        i = 0
        while i<len(timeSeries)-1:
            if timeSeries[i]+duration-1 >=timeSeries[i+1]:
                t+=timeSeries[i+1]-timeSeries[i]
            else:
                t+=duration
            i+=1
        t+=duration 
        return t
