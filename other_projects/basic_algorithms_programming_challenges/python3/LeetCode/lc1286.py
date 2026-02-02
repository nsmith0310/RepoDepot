from itertools import combinations as c

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.com = list(c(characters,combinationLength))
        self.l = [''.join(x) for x in self.com]
        self.l.sort()
        self.c = len(self.l)

    def next(self) -> str:
        self.c-=1
        tmp = self.l[0]
        del self.l[0]
        return tmp

    def hasNext(self) -> bool:
        return self.c>0


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
