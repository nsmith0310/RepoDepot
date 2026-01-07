class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        
        m = 6*minutes
        
        
        if hour == 12:
            h = 0
        else:
            h = hour*30
        
        h += 30*(minutes/60)
        
        
        
        val1 = abs(m-h)
        
        l = [val1,360-val1]
        return min(l)
        
