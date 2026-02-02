class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.p=0
        self.c=0
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()
        self.c+=1
        if self.p==0:
            self.p = 1
        else:
            self.p = 0
        

    def findMedian(self) -> float:
        if self.p==1:
            return self.arr[self.c//2]
        else:
            return (self.arr[self.c//2]+self.arr[self.c//2 - 1])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
