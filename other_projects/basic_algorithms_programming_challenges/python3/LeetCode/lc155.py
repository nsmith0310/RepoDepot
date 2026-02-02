class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.lim = 0
        

    def push(self, x: int) -> None:
        self.arr.append(x)
        self.lim+=1

    def pop(self) -> None:
        if self.lim>0:
            self.lim-=1
            del self.arr[-1]
            

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return min(self.arr)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
