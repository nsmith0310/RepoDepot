class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = [set() for x in range(0,1000)]
        

    def add(self, key: int) -> None:
        self.l[key//1000].add(key)

    def remove(self, key: int) -> None:
        try:
            self.l[key//1000].remove(key)
        except:
            pass

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.l[key//1000]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
