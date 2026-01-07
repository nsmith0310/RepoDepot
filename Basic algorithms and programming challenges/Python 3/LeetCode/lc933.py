class RecentCounter:

    def __init__(self):
        self.arr = []

    def ping(self, t: int) -> int:
        self.arr.append(t)
        if t-3000<=self.arr[0]:
            return len(self.arr)
        else:
            while t-self.arr[0]>3000:
                del self.arr[0]
            return len(self.arr)
                
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
