class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr=[]
        self.size = 0
        
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.size+=1
        self.arr.insert(0,x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.size>0:
            tmp = self.arr[-1]
            self.size-=1
            del self.arr[-1]
            return tmp

    def peek(self) -> int:
        """
        Get the top element.
        """
        if self.size>0:
            return self.arr[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.size==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
