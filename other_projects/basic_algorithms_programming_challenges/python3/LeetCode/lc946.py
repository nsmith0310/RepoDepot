class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        check = [j for j in popped]
        f = []
        i = 0
        while i<len(pushed):
            
            while pushed!=[] and popped!=[] and pushed[i]==popped[0]:
                
                f.append(popped[0])
                del popped[0]
                del pushed[i]
                if i>0:i-=1
                
                
            i+=1
        return pushed==[] and check==f
