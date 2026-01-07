class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        food = set()
        ###print(orders)
        mx = 0
        i = 0
        while i<len(orders):
            if int(orders[i][1])>mx:mx=int(orders[i][1])
            food.add(orders[i][2])
            i+=1
        
        head = list(food)
        head.sort()
        
        lim = len(head)
        l = [[0 for i in range(0,lim)] for x in range(0,mx)]
        tmp = [x for x in l[0]]
        i = 0
        while i<len(orders):
            l[int(orders[i][1])-1][head.index(orders[i][2])]+=1
            i+=1
        head.insert(0,"Table")
        
        f = [head]
        i = 0
        while i<len(l):
            if l[i]!=tmp:
                l[i].insert(0,i+1)
                s = list(map(str,l[i]))
                f.append(s)
            i+=1
        return f
        
        
        
        
