class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        nums = [50001 for i in range(0,max(rating))]
        
        
        i = 0
        while i<len(rating):
            nums[rating[i]-1]=i
            i+=1
        
        pos = []
        for x in nums:
            if x<50001:
                pos.append(x)
        print(pos)
        
        l1 = []
        l2 = []
        
        
        f1 = [0 for i in range(0,200)]
        f2 = [0 for i in range(0,200)]
        
        b1 = [0 for i in range(0,200)]
        b2 = [0 for i in range(0,200)]
        
        i = 0
        while i<len(pos)-1:
            j = i+1
            while j<len(pos):
                if pos[i]<pos[j]:
                    
                    f1[pos[i]]+=1
                    f2[pos[j]]+=1
                    
                if pos[0-i-1]<pos[0-j-1]:
                    b1[pos[0-i-1]]+=1
                    b2[pos[0-j-1]]+=1
                j+=1
            i+=1
            
        t = 0
        i = 0
        while i<len(f1):
            t+=f1[i]*f2[i]
            i+=1
        i = 0
        while i<len(b1):
            t+=b1[i]*b2[i]
            i+=1
        return t
        
        
