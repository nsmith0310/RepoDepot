class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        l = [i for i in range(1,n+1)]
        f = []
        i = 0
        while target!=[]:
            
            if l[0]==target[i]:
                f.append("Push")
                del l[0]
                del target[0]
            else:
                while l[0]!=target[0]:
                    f.append("Push")
                    f.append("Pop")
                    del l[0]
        return f
            
                
