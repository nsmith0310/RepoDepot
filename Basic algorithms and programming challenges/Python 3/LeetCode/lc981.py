class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict()
        self.d2 = dict()
        self.c = dict()
        self.mx = 0
        self.mn = 999999999999999
    def set(self, key: str, value: str, timestamp: int) -> None:
        try:
            self.d[key].append(value)
            
            self.d2[key][-1][1]=timestamp-1
            
            self.d2[key].append([timestamp,timestamp])
            
            self.c[key]+=1
            
            if timestamp >=self.mx:
                self.mx = timestamp
            if timestamp <=self.mn:
                self.mn = timestamp
        except:
            
            self.d[key]=[value]
            self.d2[key]=[[timestamp,timestamp]]
            self.c[key]=1
            
            if timestamp >=self.mx:
                self.mx = timestamp
            if timestamp <=self.mn:
                self.mn = timestamp
                
    def get(self, key: str, timestamp: int) -> str:
        
        
        if timestamp<self.mn:
            
            return ""
        if timestamp>self.mx:
            return self.d[key][-1]
        try:
            l = 0
            h = self.c[key]
            m = (l+h)//2
            while l<=h:
                
                if timestamp>=self.d2[key][m][0] and timestamp<=self.d2[key][m][1]:
                    return self.d[key][m]
                elif timestamp<self.d2[key][m][0]:
                    h = m-1
                    m = (l+h)//2
                else:
                    l = m+1
                    m = (l+h)//2
            return self.d[key][-1]
        except:
            
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
