class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s1 = ransomNote
        
        s2 = list(set(magazine))
        s3 = list(set(s1))
        
        for x in s3:
            if x not in s2 or s1.count(x)>magazine.count(x):
                return False
        return True
        
        
