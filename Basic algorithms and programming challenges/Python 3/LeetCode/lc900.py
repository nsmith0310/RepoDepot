class RLEIterator:

    def __init__(self, A: List[int]):
        self.t=0
        i = 0
        while i<len(A):
            if A[i]==0:
                del A[i]
                del A[i]
                i-=2
            else:
                self.t+=A[i]
            i+=2
        self.A=A
        self.c=len(self.A)
        
        
    def next(self, n: int) -> int:
        if n>=self.t:
            self.t-=n
            return -1
        
        while n>=self.A[0]:
            n-=self.A[0]
            tmp = self.A[1]
            self.t-=self.A[0]
            if self.t==0:
                break
            del self.A[0]
            del self.A[0]
            
        if n==0:    
            return tmp
        self.t-=n
        self.A[0]-=n
        return self.A[1]
        
            
        
            
        
        
        
            
                
                
            
            


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
