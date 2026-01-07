class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        if len(s)==1:
            return 1
        
        mx = 1
        i = 0
        while i<len(s)-1:
            j = i+1
            
            while j<len(s):
                if s[j]==s[i]:
                    break
                if s[j] in s[i:j]:
                    break
                if j-i+1>mx:
                    mx = j-i+1
                j+=1
            i+=1
        return mx
                
