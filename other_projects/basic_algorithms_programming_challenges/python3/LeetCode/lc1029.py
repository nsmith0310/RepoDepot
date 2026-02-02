class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        lim = len(costs)
        a_lim = lim//2
        b_lim = a_lim
        costs.sort(key=lambda x: abs(x[0]-x[1]))
        c = 0
        for i in range(lim-1,-1,-1):
            if costs[i][0]<costs[i][1]:
                if a_lim>0:
                    c+=costs[i][0]
                    a_lim-=1
                else:
                    c+=costs[i][1]
                    b_lim-=1
            else:
                if b_lim>0:
                    c+=costs[i][1]
                    b_lim-=1
                else:
                    c+=costs[i][0]
                    a_lim-=1
                    
        return c
                    
