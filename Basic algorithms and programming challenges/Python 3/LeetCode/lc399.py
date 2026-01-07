class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        d = set()
        c = 0
        for x in equations:
            
            d.add(x[0])
            d.add(x[1])
            val1 = values[equations.index(x)]
            for y in equations:
                
                if x!=y:
                    val2 = values[equations.index(y)]
                    if x[1]==y[0] and [x[0],y[1]]:
                        equations.append([x[0],y[1]])
                        values.append(val1*val2)
                        
        for x in equations:
            val1 = values[equations.index(x)]
            for y in equations:
                if x!=y:
                    val2 = values[equations.index(y)]
                    if x[1]==y[1]:
                        if [x[0],y[0]] not in equations:
                            
                            equations.append([x[0],y[0]])
                            values.append(val1/val2)
        for x in equations:
            val1 = values[equations.index(x)]
            for y in equations:
                if x!=y:
                    val2 = values[equations.index(y)]
                    if x[0]==y[0]:
                        if [x[1],y[1]] not in equations:
                            
                            equations.append([x[1],y[1]])
                            values.append(val2/val1)
                                        
        eq2=[]      
        val2=[]
        for x in equations:
            tmp = values[equations.index(x)]
            eq2.append(x[::-1])
            val2.append(1/tmp)
            
        equations+=eq2
        values+=val2
        
        d2 = list(d)
        for x in d2:
            equations.append([x,x])
            values.append(1)
        
        
        f = []
        
        i = 0
        while i<len(queries):
            try:
                f.append(values[equations.index(queries[i])])
            except:
                f.append(-1)
            i+=1
        return f
                
                
            
