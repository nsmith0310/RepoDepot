class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        
        
        i = 0
        while i<len(prices)-1:
            
            j = i+1
            if prices[j]>prices[i]:
                while j<len(prices):
                    if prices[j]-prices[i]>mx:
                        mx = prices[j]-prices[i]
                    j+=1
            i+=1
        return mx
