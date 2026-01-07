class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        
        stones.sort(reverse=True)
        
        while len(stones)>=1:
            if stones[0]!=stones[1]:
                stones.append(stones[0]-stones[1])
    
            del stones[0]
            del stones[0]
            if len(stones)<2:
                break
            stones.sort(reverse=True)
                
        
        if len(stones)==1:
            return stones[0]
        else:
            return 0
