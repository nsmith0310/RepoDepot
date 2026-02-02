from itertools import product as p
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        l = list(tiles)
        l2=set()
        k = list(set(l))
        k1 = [[tiles.count(x),x] for x in k]
        
        i = 1
        while i<=len(tiles):
            tmp = list(p(tiles,repeat=i))
            for y in tmp:
                t = 0
                s = ''.join(y)
                for z in k1:
                    if s.count(z[1])>z[0]:
                        t = 1
                        break
                if t==0:
                    l2.add(s)
                
            i+=1
        return len(list(l2))
        
        
        
