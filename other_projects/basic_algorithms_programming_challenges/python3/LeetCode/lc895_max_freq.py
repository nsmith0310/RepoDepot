class FreqStack:

    def __init__(self):
        self.f = dict()
        self.i = dict()
        self.mx = 0
        
    def push(self, x: int) -> None:
        
        try:
            self.f[x]+=1    
        except:
            self.f[x]=1
            
        if self.mx<self.f[x]:
            self.mx = self.f[x]
        
        try:
            self.i[self.f[x]].append(x)
        except:
            self.i[self.f[x]]=[x]
        
            
    def pop(self) -> int:
        
        r = self.i[self.mx].pop()
        
        self.f[r]-=1
        if self.f[r]==0:
            del self.f[r]
        if self.i[self.mx]==[]:
            self.mx-=1
        return r
        
        
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
