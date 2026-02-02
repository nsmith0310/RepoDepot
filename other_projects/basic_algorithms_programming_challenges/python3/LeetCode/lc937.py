class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        
        words = []
        nums = []
        
        for x in logs:
            y = x.split(" ")
            try:
                case = int(y[-1])
                nums.append(x)
            except:
                tmp = y[0]
                del y[0]
                y.append(tmp)
                
                words.append(' '.join(y))
        words.sort()
        
        final = []
        
        for x in words:
            y = x.split(" ")
            tmp = y[-1]
            del y[-1]
            y.insert(0,tmp)
            final.append(' '.join(y))
            
        for x in nums:
            final.append(x)
        return final
