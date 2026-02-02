class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        
        
        
        num1 = tree[0]
        num2 = -1
        i = 0
        while i<len(tree):
            if tree[i]!=num1:
                num2 = tree[i]
                break
            i+=1
        if num2==-1:return len(tree)
        
        mx = 0
        c = 0
        
        ind1 = 0
        ind2 = 1
        
        i = 0
        while i<len(tree):
            c+=1
            num3 = tree[i]
            if num3!=num2 and num3!=num1:
                if c-1>mx:
                    
                    mx = c-1
                    
                if tree[i-1]==num1:
                    num2 = num3
                    c = i-ind2
                    ind2 = i
                else:
                    num1 = num3
                    c = i-ind1
                    ind1=i
                    
            
            else:
                if num3==num1:
                    ind1=i
                else:
                    ind2=i
            if c>mx:
                
                mx = c
            
            
            i+=1
        
        return mx
            
            
            
            
