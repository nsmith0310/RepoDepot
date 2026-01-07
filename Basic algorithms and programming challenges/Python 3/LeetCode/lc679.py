from itertools import product as p,permutations

class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        n = list(map(str,nums))
        ops = list(p(["/","*","-","+"],repeat=3))
        
        br = [["(","n","o","n","o","n",")","o","n"],
        ["((","n","o","n",")","o","n",")","o","n"],
        ["(","n","o","(","n","o","n","))","o","n"],
        ["n","o","n","o","n","o","n"],
        ["n","o","(","n","o","n","o","n",")"],
        ["n","o","((","n","o","n",")","o","n",")"],
        ["n","o","(","n","o","(","n","o","n","))"],
        ["(","n","o","n",")","o","n","o","n"],
        ["n","o","(","n","o","n",")","o","n"],
        ["(","n","o","n",")","o","(","n","o","n",")"],
        ["n","o","n","o","(","n","o","n",")"]]
        
        ns = list(permutations(n))
        
        
        for x in ns:
            for y in ops:
                for q in br:
                    z = [m for m in q]
                    
                    z[z.index("n")]=x[0]
                    z[z.index("n")]=x[1]
                    z[z.index("n")]=x[2]
                    z[z.index("n")]=x[3]
                    
                    z[z.index("o")]=y[0]
                    z[z.index("o")]=y[1]
                    z[z.index("o")]=y[2]
                    
                    try:
                        if round(eval(''.join(z)),5)==24:return True
                        
                        
                    except:
                        pass
        return False
