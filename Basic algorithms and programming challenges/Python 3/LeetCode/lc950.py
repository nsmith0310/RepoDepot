class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        l = deck
        l.sort(reverse=True)
        f = [l[0]]
        
        i = 1
        while i<len(l):
            
            tmp = f[-1]
            
            f.insert(0,tmp)
            del f[-1]
            f.insert(0,l[i])
            i+=1
        return f
            
