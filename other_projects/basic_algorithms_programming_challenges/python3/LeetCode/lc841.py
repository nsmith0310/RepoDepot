class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        c = 0
        
        unlocked = set([x for x in rooms[0]])
        unlocked.add(0)
        if len(list(unlocked))==1:
            if len(rooms)==1:
                return True
            else:
                return False
            
        keys = set([x for x in rooms[0]])
        while 1!=-1:
            t = 0
            l = len(list(keys))
            newKeys = set()
            for x in keys:
                tmp = rooms[x]
                unlocked.add(x)
                
                for y in tmp:
                    newKeys.add(y)
                
            for x in newKeys:
                keys.add(x)
            if len(list(keys))==l:
                break
        print(unlocked)
        return len(list(unlocked))==len(rooms)
            
            
        
        
