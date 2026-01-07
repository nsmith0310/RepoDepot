class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict()
        self.arr = [set() for i in range(0,26)]
        

    def insert(self, key: str, val: int) -> None:
        self.d[key]=val
        self.arr[ord(key[0])-97].add(key)

    def sum(self, prefix: str) -> int:
        
        ind = ord(prefix[0])-97
        
        a = list(self.arr[ind])
        
        t = 0
        l = len(prefix)
        i = 0
        while i<len(a):
            if a[i][:l]==prefix:
                t+=self.d[a[i]]
            i+=1
        return t


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
