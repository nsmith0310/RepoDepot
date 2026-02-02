class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        lim = len(hand)
        if lim%W!=0:return False
        
        hand.sort()
        
        while lim>0:
            tmp = [hand[0]]
            del hand[0]
            lim-=1
            c = 1
            while c<W:
                try:
                    ind = hand.index(tmp[-1]+1)
                    tmp.append(hand[ind])
                    del hand[ind]
                    lim-=1
                    c+=1
                except:
                    return False
            
            
            
        return True
