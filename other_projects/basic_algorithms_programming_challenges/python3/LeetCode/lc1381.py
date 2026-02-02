class CustomStack:

    def __init__(self, maxSize: int):
        self.lim = maxSize
        self.size = 0
        self.arr=[]
        
    def push(self, x: int) -> None:
        if self.size<self.lim:
            self.arr.append(x)
            self.size+=1

    def pop(self) -> int:
        
        if self.size!=0:
            
            tmp = self.arr[-1]
            del self.arr[-1]
            self.size-=1
            return tmp
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        
        if k>self.size:
            for i in range(0,self.size):
                self.arr[i]+=val
        else:
            for i in range(0,k):
                self.arr[i]+=val
                
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
