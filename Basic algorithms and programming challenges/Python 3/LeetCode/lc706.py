class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = [-1 for i in range(0,10000)]
        self.vals = [-1 for i in range(0,10000)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        
        
        try:
            self.vals[self.keys.index(key)] = value
        except:
            
            ind = self.keys.index(-1)
            self.keys[ind]=key
            self.vals[ind]=value
        
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        try:
            return self.vals[self.keys.index(key)]
            
        except:
            return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        try:
            ind = self.keys.index(key)
            self.vals[ind]=-1
            self.keys[ind]=-1
        except:
            pass

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
