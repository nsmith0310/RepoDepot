from itertools import combinations as c
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        l = ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
        
        l2 = list(c(l,num))
        
        final = []
        for x in l2:
            z = 0
            hours = 0
            minutes = 0
            for y in x:
                
                col = y.index(":")
                hr = int(y[:col])
                mn = int(y[col+1:])
                hours+=hr
                minutes+=mn
            if minutes<10:
                z = 1
            if hours==0:
                if minutes<60:
                    if z==0:
                        final.append("0:"+str(minutes))
                    else:
                        final.append("0:0"+str(minutes))
            if minutes==0:
                if hours<12:
                    final.append(str(hours)+":00")
            else:
                if hours<12 and minutes<60:
                    if z==0:
                        final.append(str(hours)+":"+str(minutes))
                    else:
                        final.append(str(hours)+":0"+str(minutes))
            
        
        return list(set(final))
                
                
