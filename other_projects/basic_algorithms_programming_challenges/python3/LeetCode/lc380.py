from random import randint

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = set()
        self.lim = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        
        if val in self.vals:
            return False
        else:
            self.vals.add(val)
            self.lim+=1
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.vals:
            return False
        else:
            self.vals.remove(val)
            self.lim-=1
            return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        unf = list(self.vals)
        ###print(self.lim,unf)
        return unf[randint(0,self.lim-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
