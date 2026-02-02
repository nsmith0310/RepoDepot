class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.deque = []
        self.lim = 0
        self.cap = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.lim<self.cap:
            self.deque.insert(0,value)
            self.lim+=1
            
            return True
        else:
            return False
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.lim<self.cap:
            self.deque.append(value)
            self.lim+=1
            return True
        else:
            return False
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.lim>0:
            del self.deque[0]
            self.lim-=1
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.lim>0:
            del self.deque[-1]
            self.lim-=1
            return True
        else:
            return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.lim>0:
            return self.deque[0]
        else:
            return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.lim>0:
            return self.deque[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.lim==0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.lim==self.cap


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
