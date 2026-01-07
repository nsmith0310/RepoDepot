from copy import copy
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        lim = len(graph)-1
        f = []
        start = [[x] for x in graph[0]]
        if [lim] in start:
            f.append([0,lim])
        for x in start:
            for y in graph[x[-1]]:
                if y==lim:
                    tmp = copy(x)
                    tmp.append(lim)
                    tmp.insert(0,0)
                    f.append(tmp)
                else:
                    tmp = copy(x)
                    tmp.append(y)
                    start.append(tmp)
                    
        return f
            
