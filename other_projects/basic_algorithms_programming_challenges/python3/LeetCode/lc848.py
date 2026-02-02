class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        shiftsb = []
        
        i = 0
        while i<len(shifts):
            shiftsb.append(sum(shifts[i:]))
            i+=1
        
        s = list(S)
        i = 0
        while i<len(S):
            

            inc = (shiftsb[i]+ord(s[i])-97)%26
            
            s[i]=chr(inc+97)
            
            i+=1
        return ''.join(s)
