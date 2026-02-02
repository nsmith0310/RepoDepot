class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        t = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        l=[]
        u = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        
        final = []
        for x in words:
            tmp=list(x)
            s=''
            for y in tmp:
                s+=t[u.index(y)]
            final.append(s)
        return len(list(set(final)))
