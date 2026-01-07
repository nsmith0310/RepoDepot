class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        i = 0
        while i<=len(bits)-3:
            
            if bits[i]==1 and bits[i+1]==0:
                bits=bits[i+2:]
                i = 0
            elif bits[i]==1 and bits[i+1]==1:
                bits=bits[i+2:]
                i=0
            elif bits[i]==0:
                bits=bits[i+1:]
                i=0
            
        return list(set(bits))==[0]
                
                    
            
