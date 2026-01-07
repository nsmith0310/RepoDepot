class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = cost[::-1]
        
        p1 = 0
        p2 = 0
        
        for i in range(0,len(cost)):
            tmp = p1
            p1 = cost[i]+min(p1,p2)
            p2 = tmp
            
            
            
            
        return min(p1,p2)
            
        
        
