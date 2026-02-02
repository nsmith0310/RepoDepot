class LRUCache:

    def __init__(self, capacity: int):
        self.k = []
        self.v = []
        self.c = 0
        self.cap = capacity
    def get(self, key: int) -> int:
        try:
            ind = self.k.index(key)
            val = self.v[ind]
            del self.k[ind]
            del self.v[ind]
            self.k.append(key)
            self.v.append(val)
            return val
        except:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.c==self.cap:
            try:
                ind = self.k.index(key)
                val = self.v[ind]
                del self.k[ind]
                del self.v[ind]
                self.k.append(key)
                self.v.append(value)
                
            except:
                del self.k[0]
                del self.v[0]
                self.k.append(key)
                self.v.append(value)
        else:
            try:   
                ind = self.k.index(key)
                val = self.v[ind]
                del self.k[ind]
                del self.v[ind]
                self.k.append(key)
                self.v.append(value)
                
            except:
                self.k.append(key)
                self.v.append(value)
                self.c+=1
        
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
